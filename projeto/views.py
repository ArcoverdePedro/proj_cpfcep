from django.shortcuts import render
from django.http import JsonResponse
from .utils import validador
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def validarcpf(request):
    if request.method == 'POST':
        cpf_number = request.POST.get('cpf')
        if validador(cpf_number):
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error'})
