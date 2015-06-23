from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
	# when including urls from another app, leave the ^ and $ in the main urls.py, such as --> url(r'', include('creation.urls')),
	# and in the app's urls.py include them both such as, r'^$' or r'^snaps/$'
    url(r'^$', 'creation.views.home', name='home'),
    url(r'^blog/$', 'creation.views.blog', name='blog'),
    url(r'^blog/(?P<blog_pk>\d+)/$', 'creation.views.blog_detail', name='blog_detail'),
    url(r'^illustration/$', 'creation.views.illustration', name='illustration'),
    url(r'^illustration/(?P<illustration_pk>\d+)/$', 'creation.views.illustration_detail', name='illustration_detail'),
    url(r'^inspiration/$', 'creation.views.inspiration', name='inspiration'),
    url(r'^inspiration/(?P<inspiration_pk>\d+)/$', 'creation.views.inspiration_detail', name='inspiration_detail'),
    url(r'^fashion/$', 'creation.views.fashion', name='fashion'),
    url(r'^fashion/(?P<fashion_pk>\d+)/$', 'creation.views.fashion_detail', name='fashion_detail'),
    url(r'^snaps/$', 'creation.views.snaps', name='snaps'),
    url(r'^about/$', 'creation.views.about', name='about'),
)