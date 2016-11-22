from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^$', views.index, name='index'),
    
    # /i
    #
    url(r'^(?P<Session>[0-9]+)/$', views.view_Session, name="view_Session"),

    url(r'^$', views.view_Document, name="view_Document"),

    ]


