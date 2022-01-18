from unicodedata import name
from django.shortcuts import render
from frexcoapi import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

@csrf_exempt 
def get_region(request):                    
    try:
        if request.method == 'GET':
            regioes = models.Region.objects.all().values()
            regioes = list(regioes)
            return JsonResponse(regioes, safe=False, status=200)
        
        else:
            return JsonResponse({'mensagem' : 'O método passado não é do tipo GET.'}, status=405)
    except Exception as e:
        print(e)
        return JsonResponse({'mensagem' : 'Ocorreu um erro inesperado.'}, status=500)



@csrf_exempt
def get_fruit(request):                     
    try:
        if request.method == 'GET':
            fruits = models.Fruit.objects.all().values()
            fruits = list(fruits)
            return JsonResponse(fruits, safe=False, status=200)

        else:
            return JsonResponse({'mensagem': 'O método passado não é do tipo GET.'}, status=405)
    except Exception as e:
        print(e)
        return JsonResponse({'mensagem' : 'Ocorreu um erro inesperado.'}, status=500)




@csrf_exempt     #PEGAR FRUTAS POR REGIÃO
def get_fruit_region(request):
    try:
        if request.method == 'GET':
            pega_id = request.GET.get('regionid', 0)  
            try:
                frutas_regiao = models.Fruit.objects.filter(regionid=pega_id).values()
            except:
                return JsonResponse({'mensagem' : 'O ID consultado não é permitido.'}, status=400)


            frutas_regiao = list(frutas_regiao)
            return JsonResponse(frutas_regiao, safe=False, status=200)

        else:
            return JsonResponse({'mensagem': 'O método passado não é do tipo GET.'}, status=405)
    except Exception as e:
        print(e)
        return JsonResponse({'mensagem' : 'Ocorreu um erro inesperado.'}, status=500)



@csrf_exempt    #PEGAR REGIÃO POR ID
def get_region_id(request):
    try:
        if request.method == 'GET':
            pega_regiao_id = request.GET.get('regionid', 0)
            try:
                regioes_id = models.Region.objects.filter(id=pega_regiao_id).values()
            except:
                return JsonResponse({'mensagem' : 'O ID consultado não é permitido.'}, status=400)
            try:
                regioes_id = list(regioes_id)[0]
            except:
                return JsonResponse({'mensagem' : 'Não existe uma região com esse ID.'}, status=404)
            return JsonResponse(regioes_id, status=200)

        else:
            return JsonResponse({'mensagem': 'O método passado não é do tipo GET.'}, status=405)

    except Exception as e:
        print(e)
        return JsonResponse({'mensagem' : 'Ocorreu um erro inesperado.'}, status=500)


@csrf_exempt
def get_fruit_id(request):
    try:
        if request.method == 'GET':
            pega_fruit_id = request.GET.get('fruitid', 0)
            try:
                fruit_id = models.Fruit.objects.filter(id=pega_fruit_id).values()
            except:
                return JsonResponse({'mensagem' : 'O ID consultado não é permitido.'}, status=400)
            try:
                fruit_id = list(fruit_id)[0]
            except:
                return JsonResponse({'mensagem': 'Não existe uma fruta com esse ID.'}, status=404)
            
            return JsonResponse(fruit_id, safe=False, status=200)
        else:
            return JsonResponse({'mensagem': 'O método passado não é do tipo GET.'}, status=405)

    except Exception as e:
        print(e)
        return JsonResponse({'mensagem' : 'Ocorreu um erro inesperado.'}, status=500)



@csrf_exempt
def post_fruit(request):
    try:
        if request.method == 'POST':
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
        else:
            return JsonResponse({'mensagem': 'O método passado não é do tipo POST.'}, status=405)
    
    except Exception as e:
        print(e)
        return JsonResponse({'mensagem' : 'Ocorreu um erro inesperado.'}, status=500)



@csrf_exempt
def put_fruit(request):
    try:
        if request.method == 'PUT':
            json_data = json.loads(request.body)
            id_fruta = json_data['fruitid']
            novo_nome = json_data['newname']
            try:
                fruit = models.Fruit.objects.filter(id=id_fruta)[0]
            except:
                return JsonResponse({'mensagem' : 'O ID da fruta não foi encontrado.'}, status=404)
            fruit.name = novo_nome
            fruit.save(force_update=True)
            return JsonResponse({'mensagem' : 'Fruta atualizada com sucesso.'}, status=201)
        else:
            return JsonResponse({'mensagem': 'O método passado não é do tipo PUT.'}, status=405)
    except Exception as e:
        print(e)
        return JsonResponse({'mensagem' : 'Ocorreu um erro inesperado.'}, status=500)



@csrf_exempt
def delete_fruit(request):
    try:
        if request.method == 'DELETE':
            json_data = json.loads(request.body)
            id_fruta = json_data['fruitid']
            try:
                fruit = models.Fruit.objects.filter(id=id_fruta)[0]
            except:
                return JsonResponse({'mensagem' : 'O ID da fruta não foi encontrado.'}, status=404)
            fruit.delete()
            return JsonResponse({'mensagem' : 'Fruta excluída com sucesso.'})
        else:
                return JsonResponse({'mensagem': 'O método passado não é do tipo DELETE.'}, status=405)
    except Exception as e:
        print(e)
        return JsonResponse({'mensagem' : 'Ocorreu um erro inesperado.'}, status=500)
