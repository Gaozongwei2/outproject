from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
import json
from . import models
import time
from datetime import datetime
# Create your views here.
# 查询所有的游记``
def searchall(request):

    try:
        travelnotes = models.travelnote.objects.filter().values("title","good","view","state","cover__url")
        return HttpResponse(travelnotes)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code":"500"})
# 根据id查询游记
def searchbyuserid(request,userid):
    try:
        print("hello")
        # mytravelnotes = models.travelnote.objects.filter(userid = userid).values("title","time","","cover__url","state","good","view","condition__condition")
        # mytravelnotes = list(mytravelnotes)
        # for item in mytravelnotes:
        #     item["time"] = item["time"].strftime("%Y-%m-%d")
        # mytravelnotes = json.dumps(mytravelnotes)
        # return HttpResponse(mytravelnotes)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code":"500"})





# 普通搜索功能
def searchbysome(request):
    pass