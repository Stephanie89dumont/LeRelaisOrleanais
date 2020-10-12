from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def pourvs(request):
    message = "test test test !"
    return HttpResponse(message)

#def index(request):
# 	template = loader.get_template('pourvous/index.html')
# 	return HttpResponse(template.render(request=request))

def index(request):
 	return render(request, 'pourvous/index.html')


def Pres(request):
    return render(request, 'pourvous/Pres.html')

def Vous(request):
    return render(request, 'pourvous/Vous.html')

def Agir(request):
    return render(request, 'pourvous/Agir.html')

def Soutenir(request):
    return render(request, 'pourvous/Soutenir.html')
