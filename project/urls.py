from django.conf.urls import patterns, include, url
#from rest_framework import routers
from faculty_request import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#router =routers.DefaultRouter()
#router.register(r'request',views.faculty_viewall)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
   # url(r'^',include(router.urls)),
   # url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    #url(r'^request/$',views.faculty_viewall.as_view()),
    url(r'^requests/',include('faculty_request.urls')),
    
)
