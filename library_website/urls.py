from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import RedirectView

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
from public.views import spaces as spaces_view
from results.views import results as results_view
from search.views import search as search_view 
from units.views import units as unit_view
from lib_collections.views import collections as collection_view
from wagtail.contrib.wagtailapi import urls as wagtailapi_urls
from staff.views import staff
from base.views import json_hours

urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^shib/', include('shibboleth.urls', namespace='shibboleth')),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^json-hours/', json_hours, name='json-hours'),
    url(r'^results/$', results_view, name='results'),
    url(r'^search/$', search_view, name='search'),
    url(r'^api/', include(wagtailapi_urls)),
    url(r'^spaces/$', spaces_view, name='spaces'),
    url(r'^staff/$', staff, name='staff'),
    url(r'^about/directory/$', unit_view, name='unit'),
    url(r'^collections/$', collection_view, name='collection'),

    url(r'', include(wagtail_urls)),
]

# Prepend the shibboleth logout url if the application
# is configured for shibboleth 
#if settings.SHIBBOLETH_LOGOUT_URL:
#    urlpatterns.insert(0, url(r'^admin/logout/$', RedirectView.as_view(url='/shib/logout/?target=%s', permanent=True), name='logout'), )

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
