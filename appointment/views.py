from django.shortcuts import render
from identity.models import patient, doctor
from appointment.models import register, covid
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from django.core import serializers
import datetime

# Create your views here.

@require_http_methods(['GET'])
def add_register(request):
    response={}
    try:
        year=int(request.GET.get('year'))
        month=int(request.GET.get('month'))
        day=int(request.GET.get('day'))
        date = datetime.date(year,month,day)
        tmp_p_id = request.GET.get('p_id')
        tmp_p = patient.objects.get(p_id = tmp_p_id)
        tmp_d_id = request.GET.get('d_id')
        tmp_d = doctor.objects.get(d_id = tmp_d_id)
        tmp_r = register(r_id=request.GET.get('r_id'),r_hospital=request.GET.get('r_hospital'), \
                            r_department=request.GET.get('r_department'),r_time=date,\
                            p_id=tmp_p,d_id=tmp_d)
        tmp_r.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(['GET'])
def add_covid(request):
    response={}
    try:
        year=int(request.GET.get('year'))
        month=int(request.GET.get('month'))
        day=int(request.GET.get('day'))
        date = datetime.date(year,month,day)
        type = int(request.GET.get('c_type'))
        tmp_p_id = request.GET.get('p_id')
        tmp_p = patient.objects.get(p_id = tmp_p_id)
        tmp_c = covid(c_id=request.GET.get('c_id'),c_type=type,\
                        c_hospital=request.GET.get('c_hospital'),\
                        c_time=date,p_id=tmp_p)
        tmp_c.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

