from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	# when including urls from another app, leave the ^ and $ in the main urls.py, such as --> url(r'', include('creation.urls')),
	# and in the app's urls.py include them both, such as --> url(r'^$', 'creation.views.home', name='home'), OR url(r'^snaps/$', 'creation.views.snaps', name='snaps'),
    url(r'', include('creation.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
