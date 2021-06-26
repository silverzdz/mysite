from medicine.models import Drug
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from django.core import serializers

# Create your views here.

@require_http_methods(['GET'])
def delete_drug(request):
    response = {}
    try:
        id = request.GET.get('drug_id')
        Drug.objects.get(drug_id = id).delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(['GET'])
def buy_drug(request):
    response = {}
    try:
        id = int(request.GET.get('drug_id'))
        num = int(request.GET.get('buy_num'))
        tmp = Drug.objects.get(drug_id = id)
        if(tmp.drug_inventory >= num):
            tmp.drug_inventory -= num
            tmp.save(update_fields=['drug_inventory'])
            response['msg'] = 'success'
            response['error_num'] = 0
        else:
            response['msg'] = 'Inventory not enough!'
            response['error_num'] = 2
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def add_drug(request):
    response = {}
    try:
        id = request.GET.get('drug_id')
        name = request.GET.get('drug_name')
        inventory = request.GET.get('drug_inventory')
        tmp = Drug.objects.get(drug_id=id,drug_name=name)
        tmp.drug_inventory = tmp.drug_inventory + int(inventory)
        tmp.save(update_fields=['drug_inventory'])
        response['msg'] = 'Add inventory success!'
        response['error_num'] = 0
    except Drug.DoesNotExist:
        drug = Drug(drug_name=request.GET.get('drug_name'),drug_id=int(request.GET.get('drug_id')),drug_inventory=request.GET.get('drug_inventory'))
        drug.save()
        response['msg'] = 'Add new drug success!'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_drugs(request):
    response = {}
    try:
        drugs = Drug.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", drugs))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)