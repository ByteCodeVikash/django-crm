import os
import dj_database_url
from pathlib import Path
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-yourrandomkeyhere')  # Env var se le

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']  # Yeh fix karega 400 error, .onrender.com se sab domains allow

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Your apps, jaise 'common', 'massmail', etc. yahan add kar agar nahi hain
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'crm.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# Use PostgreSQL from Render
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600, engine='django.db.backends.postgresql')
}  # Yeh MySQL ko replace karega PostgreSQL se

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Yeh Render ke liye
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Yeh alag hai STATIC_ROOT se, error fix hoga

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Your custom settings
SHIPMENT_DATE_CHECK = True

# List of fields, the value of which will be saved
# to the Excel file when exporting contact persons.
CONTACT_COLUMNS = [
    'first_name', 'last_name', 'title', 'sex', 'birth_date',
    'was_in_touch', 'phone', 'other_phone', 'mobile', 
    'email', 'secondary_email', 'city_name', 'address',
    'country', 'description', 'birth_date', 'owner',
    'company', 'department', 'disqualified', 'massmail'
]

# List of fields, the value of which will be saved
# to the Excel file when exporting companies.
COMPANY_COLUMNS = [
    'full_name', 'website', 'phone', 'city_name', 'address',
    'email', 'description', 'lead_source', 'was_in_touch',
    'country',  'owner', 'type', 'industry', 'department',
    'disqualified', 'massmail'
]

# List of fields, the value of which will be saved
# to the Excel file when exporting leads.
LEAD_COLUMNS = [
    'first_name', 'last_name', 'title', 'sex', 'birth_date',
    'was_in_touch', 'email', 'secondary_email', 'phone',
    'other_phone', 'mobile', 'city_name', 'country',
    'address', 'description', 'lead_source', 'website',
    'company_phone', 'city_name', 'company_address',
    'company_email', 'owner', 'company_name', 'department',
    'disqualified', 'massmail'
]

# List of fields, the value of which will be saved
# to the Excel file when exporting deals.
DEAL_COLUMNS = [
    'request', 'contact', 'contact__email', 'contact__phone',
    'company', 'lead', 'lead__email', 'lead__phone',
    'ticket', 'creation_date'
]

FIRST_STEP = _('Establish the first contact with the client.')


CONVERT_REQUIRED_FIELDS = (
    'first_name', 'email',      # 'last_name'
    'company_name', 'company_email'
)

KEEP_TICKET = mark_safe(
    '<br><br><br><font size="1" color="#003366">'
    'Your request is assigned a [ticket:%s].<br>'
    'Please keep it in correspondence.</font>'
)

# For IMAP connection
REUSE_IMAP_CONNECTION = False   # True - a little faster but less stable (with some IMAP servers)
IMAP_CONNECTION_IDLE = 4320     # minutes (3 days)
IMAP_NOOP_PERIOD = 4 * 60       # seconds
IMAP_DEBUG_LEVEL = 0
