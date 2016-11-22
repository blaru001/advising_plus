from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^$', views.index, name='index'),
    
    # /i
    #
    url(r'^(?P<session_id>[0-9]+)/$', views.view_Session, name="view_Session"),

    ]


