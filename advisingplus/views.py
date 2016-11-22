from django.http import Http404 
#from django.http  import HttpResponse
from django.shortcuts import render 
from .models import Session, Advisor_Timeslot  


def index(request):
    all_Sessions = Session.objects.all()
    return render(request,'advisingplus/index.html', {'all_Sessions': all_Sessions,} )


"""
def index(request):
    all_Sessions = Session.objects.all()
    context = {  'all_Sessions': all_Sessions, } 
    return render(request,'advisingplus/index.html',context)
"""
"""
from django.template import loader 
def index(request):
    all_Sessions = Session.objects.all()
    template = loader.get_template('advisingplus/index.html')
    context = { 
            'all_Sessions': all_Sessions,
            } 

    return HttpResponse(template.render(context, request))
"""

"""def index(request):
    all_Sessions = Session.objects.all()
    
    html = ''
    for session in all_Sessions:
        url = '/' + str(session.id) + '/'
        html += '<a href=' + url+ '>' + str(session) + '</a><br>'

    return HttpResponse(html)
"""

def view_Session(request, session_id):
    try:
        session = Session.objects.get(pk=session_id)
    except Session.DoesNotExist:
        raise Http404("session does not exist")
    return render(request,'advisingplus/view_Session.html', {'session':session,} ) 
