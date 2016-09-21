"""
Django settings for library_website project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bleach',

    'debug_toolbar',

    'taggit',
    'compressor',
    'modelcluster',

    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtailsearch',
    'wagtail.wagtailimages',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailsites',
    'wagtail.wagtailembeds',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    "wagtail.contrib.table_block",
    'wagtail.contrib.wagtailsearchpromotions',
    'wagtail.contrib.wagtailsitemaps',
    'wagtail.contrib.wagtailstyleguide',
    'wagtail.contrib.wagtailapi',
    
    'corsheaders',
    'rest_framework',
    'alerts',
    'ask_a_librarian',
    'base',
    'conferences',
    'dirbrowse',
    'directory_unit',
    'events',
    'findingaids',
    'group',
    'home',
    'icon_list_boxes',
    'intranetforms',
    'intranethome',
    'intranettocs',
    'intranetunits',
    'lib_collections',
    'library_website',
    'macros',
    'news',
    'public',
    'projects',
    'redirects',
    'results',
    'search',
    'shibboleth',
    'staff',
    'subjects',
    'units',
    'static_precompiler',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

    # Required for shibboleth
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'shibboleth.middleware.ShibbolethRemoteUserMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'library_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shibboleth.context_processors.login_link',
                'shibboleth.context_processors.logout_link',
            ],
        },
    },
]

WSGI_APPLICATION = 'library_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# Don't put database information here!!!


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    'static_precompiler.finders.StaticPrecompilerFinder',
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Phone number format
PHONE_FORMAT = '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
PHONE_ERROR_MSG = 'Please enter the phone number using the format 773-123-4567'

# Postal code format
POSTAL_CODE_FORMAT = '^[0-9]{5}$'
POSTAL_CODE_ERROR_MSG = 'Please enter the postal code as a five digit number, e.g. 60637'

# ORCID
ORCID_FORMAT = '^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
ORCID_ERROR_MSG = 'Please enter ORCIDs as a 16 digit number with hyphens, e.g. 1111-2222-3333-4444'

# django-compressor settings
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# django-static-precompilers 
STATIC_PRECOMPILER_COMPILERS = (
    'static_precompiler.compilers.libsass.SCSS',
)

# Wagtail settings
WAGTAIL_SITE_NAME = "library_website"

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
    	'URLS': ['http://localhost:9200'],
        'INDEX': 'wagtail',
        'TIMEOUT': 5,
    }
}

# Settings for cross origin requests
# Documentation and settings:
# https://github.com/OttoYiu/django-cors-headers
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'catalog.lib.uchicago.edu',
    'catalogtest.lib.uchicago.edu',
    'dldc1.lib.uchicago.edu',
    'dldc2.lib.uchicago.edu',
    'dldc3.lib.uchicago.edu',
    'vufindtest.lib.uchicago.edu',
    'guides.lib.uchicago.edu',
)
CORS_ALLOW_METHODS = (
    'GET',
    #'POST',
    #'PUT',
    #'PATCH',
    #'DELETE',
    #'OPTIONS'
)

# Lock down specific nodes to wagtail groups. Sections are locked down
# by page ID. In order to see any page, a user must belong to all groups
# set in all page ancestors. This works as a blacklist. 
# PERMISSIONS_MAPPING = {6: ['Library'], 319: ['Foo', 'Bar']}
PERMISSIONS_MAPPING = {6: ['Library']}

# Where to send users that aren't members of the necessary groups to
# view a page.
NO_PERMISSIONS_REDIRECT_URL = 'https://motacilla.lib.uchicago.edu/no-permission/'

# Settings for RESTful API and frontend cache invalidation
WAGTAILAPI_SEARCH_ENABLED = True
WAGTAILAPI_MAX_RESULTS = 60

# Institutional ID for libcal
LIBCAL_IID = 482

# Fallback unit for pages that don't have one (Library - Regenstein Library)
DEFAULT_UNIT = 2455

# The unit for pages that are assigned to The University of Chicago Libraries.
# In other words generic pages that are not branch library specific use this number.
ROOT_UNIT = 2455

PUBLIC_HOMEPAGE = 3378

# String templates for hours and address display in the header and footer
HOURS_TEMPLATE = '%s: %s'
ADDRESS_TEMPLATE = '%s, %s, %s %s'

# Location and hours page
HOURS_PAGE = 4084

# Library news categories
NEWS_CATEGORIES = set(['Resources', 'Research', 'Teaching', 'Events', 'Exhibits', 'People', 'Hours & Access', 'Spaces', 'Spotlight', 'From the Director'])

# SCRC special situations
SCRC_MAIN_UNIT = 2456
SCRC_ASK_PAGE = 4127

# UChicago Library Pages
REGENSTEIN_HOMEPAGE = 1797
SSA_HOMEPAGE = 1758
MANSUETO_HOMEPAGE = 1753 
CRERAR_HOMEPAGE = 1752
ECKHART_HOMEPAGE = 1755
DANGELO_HOMEPAGE = 1754
SCRC_HOMEPAGE = 1756
DISSERTATION_HOMEPAGE = 1672

# Loop Email Notification header and footer
LOOP_EMAIL_NOTIFICATION_HEADER = "Here is a round-up of some interesting Loop news stories that you may have missed."
LOOP_EMAIL_NOTIFICATION_FOOTER = "As always, contact <a href='mailto:intranet@lib.uchicago.edu'>intranet@lib.uchicago.edu</a> with any questions or feedback regarding Loop."

# Site IDs
PUBLIC_SITE = 3

# Quick numbers for directory
# Links should be integers (page ID)
# If a link is present, the phone number
# will not be used
QUICK_NUMS = {
    'the-university-of-chicago-library':
        [{'label': 'Main Telephone',               'number': '773-702-8740', 'link': None},
         {'label': 'Privileges',                   'number': '773-702-8782', 'link': None},
         {'label': 'General Reference',            'number': '773-702-4685', 'link': None}],
    'the-joseph-regenstein-library':
        [{'label': 'Main Telephone',               'number': '773-702-8740', 'link': None},
         {'label': 'Privileges',                   'number': '773-702-8782', 'link': None},
         {'label': 'General Reference',            'number': '773-702-4685', 'link': None}],
    'the-john-crerar-library':
        [{'label': 'Crerar Circulation',           'number': '773-702-7409', 'link': None},
         {'label': 'Crerar Reference',             'number': '773-702-7715', 'link': None}],
    'the-dangelo-law-library':
        [{'label': 'D\'Angelo Law Main Telephone', 'number': '773-702-9615', 'link': None},
         {'label': 'Law Circulation',              'number': '773-702-0213', 'link': None},
         {'label': 'Law Reference',                'number': '773-702-9631', 'link': None}],
    'eckhart-library':
        [{'label': 'Eckhart Library',              'number': '773-702-8778', 'link': None}],
    'the-joe-and-rika-mansueto-library':
        [{'label': 'Mansueto Circulation Desk',    'number': '773-702-0901', 'link': None}],
    'special-collections-research-center':
        [{'label': 'SCRC Front Desk',              'number': '773-702-8705', 'link': None},
         {'label': 'SCRC Contact Form',            'number': '', 'link': SCRC_ASK_PAGE}],
    'social-service-administration-library':
        [{'label': 'SSA Library',                  'number': '773-702-1199', 'link': None}],
}
