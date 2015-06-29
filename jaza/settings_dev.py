import sys
globals().update(vars(sys.modules['jaza.settings']))

DEBUG = True

COUNTRY_INFO_FILE = SITE_ROOT + 'data/countrylist.test.csv'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'morpheus',
        'USER': 'morpheus',
        'PASSWORD': 'admin',
        'HOST': '',
        'PORT': '',
    }
}
