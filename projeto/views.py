from django.shortcuts import render
from django.http import JsonResponse
from .utils import validador
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.

@csrf_exempt
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def validarcpf(request):
    if request.method == 'POST':
        cpf_number = request.POST.get('cpf')
        #verifica cpf no validador (validador cagado, fazer um bom)
        if validador(cpf_number): 
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error'})
        

@csrf_exempt
def buscarcep(request):
    if request.method == 'POST':
        cep_number = request.POST.get('cep')
        #tenta puxar o cep da api do viacep
        try :
            #faz a requisição e pega o json colocando na variavel data
            response = requests.get(f'https://viacep.com.br/ws/{cep_number}/json/') 
            data = response.json()
            return JsonResponse(data)
        except:
            #se der erro na requisição, retorna erro = true (aplicando a mesma lógica da api do viacep)
            return JsonResponse({'erro': 'true'})


      
