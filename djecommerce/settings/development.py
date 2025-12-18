from .base import *

from decouple import config  # 🔥 THIS LINE WAS MISSING

# --------------------------------------------------
# DEVELOPMENT SETTINGS
# --------------------------------------------------
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

# --------------------------------------------------
# DEBUG TOOLBAR
# --------------------------------------------------
INTERNAL_IPS = [
    '127.0.0.1',
]

# --------------------------------------------------
# EMAIL (console)
# --------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# --------------------------------------------------
# STRIPE (TEST KEYS)
# --------------------------------------------------
STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY', default='')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY', default='')
