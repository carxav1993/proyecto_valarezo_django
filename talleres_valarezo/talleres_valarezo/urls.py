from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'talleres_valarezo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.empresa.urls', namespace="empresa")),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns +=[
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,}
        ),
    ]