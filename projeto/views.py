from django.shortcuts import render
from .models import cpf
from django.http import JsonResponse
from .utils import validador
# Create your views here.

def home(request):
    return render(request, 'home.html')

def validar_cpf(request):
    if request.method == 'POST':
        cpf_number = request.POST.get('cpf')
        if validador(cpf_number):
            cpf.objects.create(cpf=cpf_number)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'error'})