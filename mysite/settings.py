import yaml
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Загрузка конфигурации из YAML-файла
def load_yaml_config(file_name):
    with open(BASE_DIR / file_name) as f:
        return yaml.safe_load(f)


config = load_yaml_config('config.yaml')

# Получаем имя текущего пользователя
CURRENT_USER = os.getlogin().lower()

# Определяем среду
if CURRENT_USER == 'user':
    DEBUG = True
    PRODUCTION = False
else:
    DEBUG = False
    PRODUCTION = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['secret_key']

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# Application definition

INSTALLED_APPS = [
    # custom applications
    'users',
    'flights',
    'corsheaders',
    'rest_framework',
    # default applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

AUTH_USER_MODEL = 'users.User'  # Указание пользовательской модели

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Настройка CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # здесь порт, на котором работает фронтенд
    "http://127.0.0.1:3000",   # фронтенд работает на этом адресе
]

ROOT_URLCONF = 'mysite.urls'

# Настройки 'Templates', которые указывают, где искать шаблоны и как их обрабатывать.
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config['database_name'],
        'USER': config['database_user'],
        'PASSWORD': config['database_password'],
        'HOST': config['database_host'],
        'PORT': config['database_port'],
    }
}

# Настройки электронной почты
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config['email_host']
EMAIL_PORT = config['email_port']
EMAIL_USE_TLS = config['email_use_tls']
EMAIL_HOST_USER = config['email_host_user']
EMAIL_HOST_PASSWORD = config['email_host_password']

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = config['timezone']

USE_I18N = True

USE_TZ = True


# URL для доступа к статическим файлам
STATIC_URL = '/static/'

# Директория, куда будут собираться статические файлы (используется на сервере)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Дополнительные директории со статическими файлами для разработки
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # директория для хранения статических файлов в процессе разработки
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRONJOBS = [
    ('0 0 * * *', 'flights.management.commands.fetch_aviasales_data')
]

