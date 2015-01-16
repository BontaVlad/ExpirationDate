from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

from expirationDate.views import HomePage, HelpPage, LicensePage

urlpatterns = patterns(
    '',
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^help$', HelpPage.as_view(), name='help'),
    url(r'^license$', LicensePage.as_view(), name='license'),
    (r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',  # noqa pylint: disable-msg=C0103
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT}))
