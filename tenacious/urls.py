from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)

urlpatterns = patterns('',
    # Home Page
    url(r'^$', 'app.views.home', name='home'),
    
    # API
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # Clients
    url(r'^clients/add','app.views.new_client', name='new_client'),

    # Matters
    url(r'^matters/add','app.views.new_matter', name='new_matter'),
    url(r'^matters/(?P<pk>[\w|-]+)/$', views.MatterUpdate.as_view(), name='matter-detail'),
    url(r'^matters/(?P<pk>[\w|-]+)/delete/$', views.MatterDelete.as_view(), name='matter-delete'),

    # Documents
    url(r'^documents/add','app.views.new_document', name='new_document'),

    # Bundles
    url(r'^bundles/add','app.views.new_bundle', name='new_bundle'),
        
    # Administrative Stuff
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'app.views.logout'),
)