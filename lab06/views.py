from django.shortcuts import render



# Create your views here.
def index(request):

    context = {
        'titulo': "Formulario",
    }
    return render(request,'tienda/index.html', context)