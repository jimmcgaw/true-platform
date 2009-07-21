import os, sys
sys.path.append('/home/smoochy/levicci')
sys.path.append('/home/smoochy/levicci/settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'levicci.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
