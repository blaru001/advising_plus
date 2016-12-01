#from django.http import Http404 
#from django.http  import HttpResponse
from django.shortcuts import render , get_object_or_404 

#class based view imports

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.views import generic 
from django.views.generic import View 
from .models import Session, Timeslot, Document  
from .forms import UserForm 



#==================================
#    sessions
#=================================

class SessionListView(generic.ListView):
    template_name = 'advisingplus/index.html'
    context_object_name = 'object_list' # can be anthing- used in template   
    def get_queryset(self):
        return Session.objects.all()
        # Session.objects.filter(id=3)

class SessionDetailView(generic.DetailView):
    model = Session
    template_name ='advisingplus/view_Session.html' 

class SessionCreate(CreateView):
    model = Session
    fields = ['timeslot', 'student']

class SessionUpdate(UpdateView):
    model = Session
    fields = ['timeslot', 'student']

class SessionDelete(DeleteView):
    model = Session
    success_url = reverse_lazy('advisingplus:session-list')

#================================
#  documents
#================================


class DocumentListView(generic.ListView):
    template_name = 'advisingplus/document_list.html'
    context_object_name = 'object_list'    
    def get_queryset(self):
        return Document.objects.all()
        # Session.objects.filter(id=3)

class DocumentDetailView(generic.DetailView):
    model = Document
    template_name ='advisingplus/view_document.html' 

class DocumentCreate(CreateView):
    model = Document
    fields = ['sessionId','doc', 'docname','requestReason']

class DocumentUpdate(UpdateView):
    model = Document
    fields = ['sessionId','doc', 'docname','requestReason']

class DocumentDelete(DeleteView):
    model = Document
    success_url = reverse_lazy('advisingplus:document-list')


#=================================
# old functional code
#=================================

'''
def index(request):
    all_Sessions = Session.objects.all()
    return render(request,'advisingplus/index.html', {'all_Sessions': all_Sessions,} )

def view_Session(request, session_id):
    session = get_object_or_404(Session,pk=session_id )
    return render(request,'advisingplus/view_Session.html', {'session':session,} ) 
'''
'''
class logout(View):
        logout(request)
        return redirect('advisingplus:index')
'''
#===============================
#user login
#===============================
class UserFormView(View):
    form_class = UserForm
    template_name = 'advisingplus/registration_form.html'

    #display blank form
    def get(self, request):
       form = self.form_class(None)
       return render(request, self.template_name, {'form': form})

   #process form data 
    def post(self, request):  
        form = self.form_class( request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #clearn (normalized ) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return user object if credentials are correct
            user = authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('advisingplus:session-list')
                    #if you need this info later use
                    # request.user.username
        
        return render(request, self.template_name, {'form': form})

