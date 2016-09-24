from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'apps.empresa.views.index', name='inicio'),
    url(r'^nosotros/', 'apps.empresa.views.nosotros', name='nosotros'),
    url(r'^servicios/', 'apps.empresa.views.servicios', name='servicios'),
    url(r'^contactenos/', 'apps.empresa.views.contactenos', name='contactenos'),
]
