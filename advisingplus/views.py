from django.http  import HttpResponse
from .models import Session, Advisor_Timeslot  

def index(request):
    all_Sessions = Session.objects.all()
    
    html = ''
    for session in all_Sessions:
        url = '/' + str(session.id) + '/'
        html += '<a href=' + url+ '>' + str(session) + '</a><br>'

    return HttpResponse(html)

def view_Session(request, Session):
    return HttpResponse('<h2> details for session:' + str(Session) + ' </h2>') 
