from django.db import models
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from modelcluster.fields import ParentalKey
from base.models import BasePage
from public.models import DonorPage, LocationPage
from staff.models import StaffPage, StaffPageSubjectPlacement
from subjects.models import Subject

# The abstract model for related links, complete with panels
class AccessLink(models.Model):
    access_link_label = models.CharField(max_length=255)
    access_link_url = models.URLField("Access link URL", blank=False)

    panels = [
        FieldPanel('access_link_label'),
        FieldPanel('access_link_url'),
    ]

    class Meta:
        abstract = True

# The real model which combines the abstract model, an
# Orderable helper class, and what amounts to a ForeignKey link
# to the model we want to add related links to (CollectionPage)
class CollectionPageAccessLinks(Orderable, AccessLink):
    page = ParentalKey('lib_collections.CollectionPage', related_name='access_links')


# Model for format strings to be used on collection pages
@register_snippet
class Format(models.Model, index.Indexed):
    text = models.CharField(max_length=255, blank=False)

    panels = [
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.text

    search_fields = [
        index.SearchField('text', partial_match=True),
    ]

# Interstitial model for linking the Format model to the CollectionPage
class CollectionPageFormatPlacement(Orderable, models.Model):
    page = ParentalKey('lib_collections.CollectionPage', related_name='collection_placements')
    format = models.ForeignKey('lib_collections.Format', related_name='+')

    class Meta:
        verbose_name = "Collection Placement"
        verbose_name_plural = "Collection Placements"

    panels = [
        SnippetChooserPanel('format'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.format.text


class CollectionPageSubjectPlacement(Orderable, models.Model):
    page = ParentalKey('lib_collections.CollectionPage', related_name='collection_subject_placements')
    subject = models.ForeignKey('subjects.Subject', related_name='+')

    class Meta:
        verbose_name = "Subject Placement"
        verbose_name_plural = "Subbject Placements"

    panels = [
        SnippetChooserPanel('subject'),
    ]

    def __str__(self):
        return self.page.title + " -> " + Subject.name


# Interstitial model for linking the DonorPages to the CollectionPage
class DonorPagePlacement(Orderable, models.Model):
    """
    Create a through table for linking donor pages to collection pages
    """
    parent = ParentalKey(
        'lib_collections.CollectionPage', 
        related_name='donor_page_list_placement', 
        null=True, 
        blank=False, 
        on_delete=models.SET_NULL
    )

    donor = models.ForeignKey(
        'public.DonorPage', 
        related_name='donor_page', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
    )

# The abstract model for alternative collection names 
class AlternateName(models.Model):
    alternate_name = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('alternate_name'),
    ]

    class Meta:
        abstract = True

# Attaches alternative names to collections.
class CollectionPageAlternateNames(Orderable, AlternateName):
    """
    Creates a through table for alternate names for CollectionPages.
    """
    page = ParentalKey('lib_collections.CollectionPage', related_name='alternate_name')

# Interstitial model for linking the collection RelatedPages to the CollectionPage
class RelatedCollectionPagePlacement(Orderable, models.Model):
    """
    Creates a through table for RelatedPages that attach to 
    the CollectionPage type. 
    """
    parent = ParentalKey(
        'lib_collections.CollectionPage', 
        related_name='related_collection_placement', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
    )

    related_collection = models.ForeignKey(
        'CollectionPage', 
        related_name='related_collection', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
    )

 
# Collection page content type
class CollectionPage(BasePage):
    """
    Pages for individual collections.
    """
    short_abstract = models.TextField(null=False, blank=False, default='')
    full_description = models.TextField(null=False, blank=False, default='')
    access_instructions = models.TextField(null=False, blank=True, default='')
    thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    ) 
    collection_location = models.ForeignKey('public.LocationPage',
        null=True, blank=True, on_delete=models.SET_NULL)
    staff_contact = models.ForeignKey('staff.StaffPage',
        null=True, blank=True, on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        InlinePanel('alternate_name', label='Alternate Names'),
        FieldPanel('short_abstract'),
        FieldPanel('full_description'),
        ImageChooserPanel('thumbnail'),
        InlinePanel('collection_subject_placements', label='Subjects'),
        InlinePanel('collection_placements', label='Formats'),
        FieldPanel('access_instructions'),
        InlinePanel('access_links', label='Access Links'),
        InlinePanel('related_collection_placement', label='Related Collection'),
        FieldPanel('collection_location'),
        InlinePanel('donor_page_list_placement', label='Donor'),
        FieldPanel('staff_contact'),
    ] + BasePage.content_panels


class SubjectSpecialistPlacement(Orderable, models.Model):
    """
    Creates a through table that connects StaffPage objects to
    the CollectionAreaPages as subject specialists .
    """
    parent = ParentalKey(
        'lib_collections.CollectingAreaPage',
        related_name='subject_specialist_placement',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    subject_specialist = models.ForeignKey(
        'staff.StaffPage',
        related_name='subject_specialist',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )


class StacksRange(models.Model):
    """
    Abstract model for call number ranges.
    """
    stacks_range = models.CharField(max_length=100, blank=True) 
    stacks_URL = models.URLField(max_length=254, blank=True, default='')

    panels = [
        FieldPanel('stacks_range'),
        FieldPanel('stacks_URL'),
    ]

    class Meta:
        abstract = True


class CollectingAreaPageStacksRanges(Orderable, StacksRange):
    """
    Create a through table for call number stacks ranges
    linked to the CollectingAreaPages.
    """
    page = ParentalKey('lib_collections.CollectingAreaPage', related_name='stacks_ranges')


class CollectingAreaReferenceLocationPlacement(Orderable, models.Model):
    """
    Through table for repeatable reference locations in the
    CollectingAreaPage content type.
    """
    parent = ParentalKey(
        'lib_collections.CollectingAreaPage',
        related_name='reference_location_placements',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    related_collection = models.ForeignKey(
        'public.LocationPage',
        related_name='reference_location',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )


class HighlightedCollectionsPlacement(Orderable, models.Model):
    """
    Through table for repeatable highlighted collections
    in the CollectingAreaPage content type.
    """
    parent = ParentalKey(
        'lib_collections.CollectingAreaPage', 
        related_name='highlighted_collection_placements', 
        null=True, 
        blank=False, 
        on_delete=models.SET_NULL
    )

    collection = models.ForeignKey(
        'CollectionPage', 
        related_name='highlighted_collections', 
        null=True, 
        blank=False, 
        on_delete=models.SET_NULL
    )


class RegionalCollection(models.Model):
    """
    Abstract model for regional collections.
    """
    collection_name = models.CharField(max_length=254, blank=True) 
    collection_description =  models.TextField(blank=True)

    panels = [
        FieldPanel('collection_name'),
        FieldPanel('collection_description'),
    ]

    class Meta:
        abstract = True


class RegionalCollectionPlacements(Orderable, RegionalCollection):
    """
    Through table for repeatable regional collection fields.
    """
    page = ParentalKey('lib_collections.CollectingAreaPage', related_name='regional_collections')



class LibGuide(models.Model):
    """
    Abstract model for lib guides.
    """
    guide_link_text = models.CharField(max_length=255, blank=False, default='')
    guide_link_url = models.URLField("Libguide URL", blank=False, default='')

    panels = [
        FieldPanel('guide_link_text'),
        FieldPanel('guide_link_url'),
    ]

    class Meta:
        abstract = True


class CollectingAreaPageLibGuides(Orderable, LibGuide):
    """
    Through table for repeatable "Other guides".
    """
    page = ParentalKey('lib_collections.CollectingAreaPage', related_name='lib_guides')


class CollectingAreaPage(BasePage, LibGuide):
    """
    Content type for collecting area pages.
    """
    subject = models.ForeignKey(
        'subjects.Subject',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_related'
    )
    collecting_statement = models.TextField(null=False, blank=False)
    #primary_guide

    content_panels = Page.content_panels + [
        FieldPanel('subject'),
        FieldPanel('collecting_statement'),
        InlinePanel('subject_specialist_placement', label='Subject Specialist'),
        InlinePanel('stacks_ranges', label='Stacks Ranges'),
        InlinePanel('reference_location_placements', label='Reference Locations'),
        InlinePanel('highlighted_collection_placements', label='Highlighted Collections'),
        InlinePanel('regional_collections', label='Regional Collections'),
        MultiFieldPanel(
            [
                FieldPanel('guide_link_text'),
                FieldPanel('guide_link_url'),
            ],
            heading='Primary Guide'
        ),
        InlinePanel('lib_guides', label='Other Guides'),
    ] + BasePage.content_panels