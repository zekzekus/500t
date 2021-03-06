
from django.conf.urls import patterns, include, url
from django.contrib import admin

from logs.views import logs, vote, add_log, login, logout, log_detail, search, random_log

# admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', logs, name='home'),
    url(r'^vote/([0-9]*?)/([1-2]*)/', vote, name="vote"),
    url(r'^add', add_log, name="add_log"),
    url(r'', include('social_auth.urls')),
    url(r'^login', login, name="login"),
    url(r'^log/([0-9]*)/', log_detail, name="log_detail"),
    url(r'^search/$', search, name="log_search"),
    url('^logout', logout, name="logout"),
    url(r'^admin/', include(admin.site.urls)),

    # api
    url(r'^api/random/', random_log, name="api_random_log"),
)
