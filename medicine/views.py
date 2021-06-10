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
        name = request.GET.get('drug_name')
        Drug.objects.get(drug_name = name).delete()
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
        name = request.GET.get('drug_name')
        num = int(request.GET.get('buy_num'))
        tmp = Drug.objects.get(drug_name = name)
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
        drug = Drug(drug_name=request.GET.get('drug_name'),drug_id=request.GET.get('drug_id'),drug_inventory=request.GET.get('drug_inventory'))
        drug.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
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