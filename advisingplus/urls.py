from django.conf.urls import url

from . import views

app_name = 'advisingplus'

urlpatterns = [ 
    url(r'^$', views.IndexView.as_view() , name='index'),
    
   #user log in 
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    
    # /i
    #
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view() , name="view_Session"),

    ]


