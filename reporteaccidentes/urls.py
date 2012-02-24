from django.conf.urls.defaults import *
from reporteaccidentes.accidentes.views import index, get_top, about, top
from django.conf import settings

urlpatterns = patterns('',
     (r'^$', index),
     (r'^update.ajax', get_top),
     (r'^ranking.html', top),
     (r'^about.html', about),
)
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()