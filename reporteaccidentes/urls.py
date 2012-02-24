from django.conf import settings
from django.conf.urls.defaults import *
from reporteaccidentes.accidentes.views import index, get_top, about, top
import django

urlpatterns = patterns('',
     (r'^$', index),
     (r'^update.ajax', get_top),
     (r'^ranking.html', top),
     (r'^about.html', about),
)

if settings.DEBUG:
    if django.VERSION[1] == 3:
        urlpatterns += staticfiles_urlpatterns()
    else:
            urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    )