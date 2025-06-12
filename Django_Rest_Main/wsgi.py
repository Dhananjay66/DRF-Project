import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Rest_Main.settings')

application = get_wsgi_application()
application = WhiteNoise(application)