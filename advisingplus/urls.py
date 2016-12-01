from django.conf.urls import url

from . import views

app_name = 'advisingplus'

urlpatterns = [
    
    #===================
    #session url
    #===============
    url(r'^session/$', views.SessionListView.as_view() , name='session-list'),
    

    #view a session
    #/2
    url(r'^session/(?P<pk>[0-9]+)/$', views.SessionDetailView.as_view() , name='session-detail'),
    

    #create a session
    # session/add/
    url(r'^session/add/$', views.SessionCreate.as_view() , name='session-add'),


    #update a session
    # session/2
    url(r'^session/update/(?P<pk>[0-9]+)/$', views.SessionUpdate.as_view() , name='session-update'),


    #delete a Session
    #session/2/delete/
    url(r'^session/(?P<pk>[0-9]+)/delete/$', views.SessionDelete.as_view() , name='session-delete'),
  
    #========================
    # documents 
    #========================

    url(r'^document/$', views.DocumentListView.as_view() , name='document-list'),
    

    #view a document
    #/2
    url(r'^document/(?P<pk>[0-9]+)/$', views.DocumentDetailView.as_view() , name='document-detail'),
    

    #create a document
    # session/add/
    url(r'^document/add/$', views.DocumentCreate.as_view() , name='document-add'),


    #update a document
    # session/2
    url(r'^document/update/(?P<pk>[0-9]+)/$', views.DocumentUpdate.as_view(), name='document-update'),


    #delete a document
    #session/2/delete/
    url(r'^documents/(?P<pk>[0-9]+)/delete/$', views.DocumentDelete.as_view() , name='document-delete'),
  
     

    #===========================
    #user log in 
    #===========================
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    
    # url(r'^logout/$', views.logout_view.as_view() , name='logout')
    ]


