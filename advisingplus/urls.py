from django.conf.urls import url

from . import views

app_name = 'advisingplus'

urlpatterns = [
    
    #----------------
    #session url
    #----------------
    url(r'^$', views.IndexView.as_view() , name='index'),
    

    #view a session
    #/2
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view() , name="view_Session"),
    

    #create a session
    # session/add/
    url(r'^session/add/$', views.SessionCreate.as_view() , name='session-add'),
    
    #update a session
    # session/2
    url(r'^session/(?P<pk>[0-9]+)/$', views.SessionUpdate.as_view() , name='session-update'),
 
    #delete a Session
    #session/2/delete/
    url(r'^session/(?P<pk>[0-9]+)/delete/$', views.SessionDelete.as_view() , name='session-delete'),
   
    #-----------------------------
    #user log in 
    #----------------------------
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    

    ]


