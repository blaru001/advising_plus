from django.http  import HttpResponse
from django.template import loader 
from .models import Session, Advisor_Timeslot  

def index(request):
    all_Sessions = Session.objects.all()
    template = loader.get_template('advisingplus/index.html')
    context = { 
            'all_Sessions': all_Sessions,
            } 

    return HttpResponse(template.render(context, request))

"""def index(request):
    all_Sessions = Session.objects.all()
    
    html = ''
    for session in all_Sessions:
        url = '/' + str(session.id) + '/'
        html += '<a href=' + url+ '>' + str(session) + '</a><br>'

    return HttpResponse(html)
"""

def view_Session(request, Session):
    return HttpResponse('<h2> details for session:' + str(Session) + ' </h2>')

def view_Document(request, Session):
    return HttpResponse('<h3> This is the Documents views </h3>') 
