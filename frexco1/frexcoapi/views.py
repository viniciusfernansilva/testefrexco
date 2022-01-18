from frexcoapi import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})


@csrf_exempt
@api_view(['GET'])
def regions(request):
    try:
        if request.method == 'GET':
            regioes = models.Region.objects.all().values()
            regioes = list(regioes)
            return JsonResponse(regioes, safe=False, status=200)
    except Exception as e:
        print(e)
        return JsonResponse({'mensagem' : 'Ocorreu um erro inesperado.'}, status=500)


   
@csrf_exempt
@api_view(['GET'])
def region_detail(request, regionid):
    try:
        if request.method == 'GET':
            try:
                region = models.Region.objects.filter(id=regionid).values()
                frutas_regiao = models.Fruit.objects.filter(regionid=regionid).values()
            except:
                return JsonResponse({'mensagem' : 'O ID consultado não é permitido.'}, status=400)
            try:
                region = list(region)[0]
                frutas_regiao = list(frutas_regiao)
            except:
                return JsonResponse({'mensagem' : 'Não existe uma região com esse ID.'}, status=404)
            response = {
                'region': region,
                'fruits': frutas_regiao
            }    
            return JsonResponse(response, status=200)
    except Exception as e:
        print(e)
        return JsonResponse({'mensagem' : 'Ocorreu um erro inesperado.'}, status=500)



@csrf_exempt
@api_view(['GET', 'POST'])
def fruits(request):
    try:
        if request.method == 'GET':
            fruits = models.Fruit.objects.all().values()
            fruits = list(fruits)
            return JsonResponse(fruits, safe=False, status=200)
        elif request.method == 'POST':
            nome_fruta = request.POST.get('namefruit')
            region_id = request.POST.get('regionid')
            try:            
                region = models.Region.objects.filter(id=region_id)[0]
            except:
                return JsonResponse({'mensagem' : 'O ID da região enviado não é permitido.'}, status=400)
            if models.Fruit.objects.filter(name=nome_fruta, regionid=region_id).exists():
                return JsonResponse({'mensagem' : 'A Fruta enviada já existe para essa região.'}, status=202)    
            try:
                fruta = models.Fruit(name=nome_fruta, regionid=region)
                fruta.save(force_insert=True)
            except:
                return JsonResponse({'mensagem' : 'Erro ao salvar os dados, verifique os campos.'}, status=400)
            return JsonResponse({'mensagem' : 'Fruta salva com sucesso.', 'fruitid' : fruta.id}, status=201)
    except Exception as e:
        print(e)
        return JsonResponse({'mensagem' : 'Ocorreu um erro inesperado.'}, status=500)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def fruit_detail(request,  fruitid):
    try:
        if request.method == 'GET':
            try:
                fruit = models.Fruit.objects.filter(id=fruitid).values()
            except:
                return JsonResponse({'mensagem' : 'O ID consultado não é permitido.'}, status=400)
            try:
                fruit = list(fruit)[0]
            except:
                return JsonResponse({'mensagem': 'Não existe uma fruta com esse ID.'}, status=404)
            
            return JsonResponse(fruit, safe=False, status=200)
        elif request.method == 'PUT':
            json_data = json.loads(request.body)
            novo_nome = json_data['newname']
            try:
                fruit = models.Fruit.objects.filter(id=fruitid)[0]
            except:
                return JsonResponse({'mensagem' : 'O ID da fruta não foi encontrado.'}, status=404)
            fruit.name = novo_nome
            fruit.save(force_update=True)
            return JsonResponse({'mensagem' : 'Fruta atualizada com sucesso.'}, status=201)
        elif request.method == 'DELETE':
            try:
                fruit = models.Fruit.objects.filter(id=fruitid)[0]
            except:
                return JsonResponse({'mensagem' : 'O ID da fruta não foi encontrado.'}, status=404)
            fruit.delete()
            return JsonResponse({'mensagem' : 'Fruta excluída com sucesso.'})
    except Exception as e:
        print(e)
        return JsonResponse({'mensagem' : 'Ocorreu um erro inesperado.'}, status=500)