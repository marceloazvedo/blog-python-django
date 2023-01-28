from django.http import HttpResponse

def index(request):
    return HttpResponse("Essa é a página da listagem de POSTs")
