from django.http import HttpResponse

def index(request):
    return HttpResponse("Hallo Welt, Karten hier!")
