from django.shortcuts import render
from identity.models import patient, doctor, merchant, admin
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from django.core import serializers
import hashlib

# Create your views here.

@require_http_methods(['GET'])
def add_patient(request):
    response = {}
    try:
        md5 = hashlib.md5()
        md5.update(request.GET.get('p_pw').encode('utf8'))
        tmp_pw = md5.hexdigest()
        tmp_p = patient(p_id=request.GET.get('p_id'),p_name=request.GET.get('p_name'),p_telephone=request.GET.get('p_telephone'),p_pw=tmp_pw)
        tmp_p.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(['GET'])
def login_patient(request):
    response = {}
    try:
        id = request.GET.get('p_id')
        md5 = hashlib.md5()
        md5.update(request.GET.get('p_pw').encode('utf8'))
        pw = md5.hexdigest()
        tmp = patient.objects.get(p_id = id)
        if(tmp.p_pw == pw):
            response['msg'] = 'Login success!'
            response['error_num'] = 0
        else:
            response['msg'] = 'Wrong password!'
            response['error_num'] = 2
    except Exception as e:
        response['msg'] = 'Id does not exist!'
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(['GET'])
def add_doctor(request):
    response = {}
    try:
        md5 = hashlib.md5()
        md5.update(request.GET.get('d_pw').encode('utf8'))
        tmp_pw = md5.hexdigest()
        tmp_d = doctor(d_id=request.GET.get('d_id'),d_name=request.GET.get('d_name'),d_telephone=request.GET.get('d_telephone'), \
                        d_hospital=request.GET.get('d_hospital'),d_department=request.GET.get('d_department'),d_pw=tmp_pw)
        tmp_d.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(['GET'])
def login_doctor(request):
    response = {}
    try:
        id = request.GET.get('d_id')
        md5 = hashlib.md5()
        md5.update(request.GET.get('d_pw').encode('utf8'))
        pw = md5.hexdigest()
        tmp = doctor.objects.get(d_id = id)
        if(tmp.d_pw == pw):
            response['msg'] = 'Login success!'
            response['error_num'] = 0
        else:
            response['msg'] = 'Wrong password!'
            response['error_num'] = 2
    except Exception as e:
        response['msg'] = 'Id does not exist!'
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(['GET'])
def add_merchant(request):
    response = {}
    try:
        md5 = hashlib.md5()
        md5.update(request.GET.get('m_pw').encode('utf8'))
        tmp_pw = md5.hexdigest()
        tmp_m = merchant(m_id=request.GET.get('m_id'),m_name=request.GET.get('m_name'),m_telephone=request.GET.get('m_telephone'),m_pw=tmp_pw)
        tmp_m.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(['GET'])
def login_merchant(request):
    response = {}
    try:
        id = request.GET.get('m_id')
        md5 = hashlib.md5()
        md5.update(request.GET.get('m_pw').encode('utf8'))
        pw = md5.hexdigest()
        tmp = merchant.objects.get(m_id = id)
        if(tmp.m_pw == pw):
            response['msg'] = 'Login success!'
            response['error_num'] = 0
        else:
            response['msg'] = 'Wrong password!'
            response['error_num'] = 2
    except Exception as e:
        response['msg'] = 'Id does not exist!'
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(['GET'])
def add_admin(request):
    response = {}
    try:
        md5 = hashlib.md5()
        md5.update(request.GET.get('a_pw').encode('utf8'))
        tmp_pw = md5.hexdigest()
        print(tmp_pw)
        tmp_a = admin(a_id=request.GET.get('a_id'),a_pw=tmp_pw)
        tmp_a.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(['GET'])
def login_admin(request):
    response = {}
    try:
        id = request.GET.get('a_id')
        md5 = hashlib.md5()
        md5.update(request.GET.get('a_pw').encode('utf8'))
        pw = md5.hexdigest()
        tmp = admin.objects.get(a_id = id)
        if(tmp.a_pw == pw):
            response['msg'] = 'Login success!'
            response['error_num'] = 0
        else:
            response['msg'] = 'Wrong password!'
            response['error_num'] = 2
    except Exception as e:
        response['msg'] = 'Id does not exist!'
        response['error_num'] = 1
    return JsonResponse(response)