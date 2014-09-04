from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hpd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^probe/$', 'hpd.demo.views.probe', name='probe'),
    url(r'^profile/(?P<pk>\d+)/$', 'hpd.demo.views.profile', name='profile'),
    url(r'^profile/create/$', 'hpd.demo.views.create_profile', name='create-profile'),
    url(r'^company/(?P<pk>\d+)/$', 'hpd.demo.views.company', name='company'),
    url(r'^job-title/(?P<pk>\d+)/$', 'hpd.demo.views.job_title', name='job-title'),
    url(r'^$', 'hpd.demo.views.home', name='home'),
)
