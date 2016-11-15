from django.http  import HttpResponse


def index(request):
    return HttpResponse("<h3> This is the request service</h3>")
