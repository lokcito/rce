from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)


def kinesiologo(request):
    context = {
        
    }
    return render(request, "kinesiologo.html", context)


def deportista(request):
    context = {}
    return render(request, "deportista.html", context)


def atencion(request):
    context = {}
    return render(request, "atencion.html", context)





