import os, sys
sys.path.append('/home/smoochy/trueplatform')
sys.path.append('/home/smoochy/trueplatform/settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'trueplatform.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
