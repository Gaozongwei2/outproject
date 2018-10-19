from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from . import models
import json

# Create your views here.
# 根据id查询攻略
def searchbyuserid(request,userid):
    try:
        mystrategys = models.strategy.objects.filter(userid = userid).values("title","time","scover__url","state","good","view","sccontent__contents","condition__condition")
        mystrategys = list(mystrategys)
        print(mystrategys)
        for item in mystrategys:
            item["time"] = item["time"].strftime("%Y-%m-%d")
        mystrategys = json.dumps(mystrategys)

        return HttpResponse(mystrategys)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code":"500"})




def insertdetail(request):
    if request.method == "GET":
        data = models.test.objects.filter().values()
        return HttpResponse(data)
    if request.method == 'POST':
        print(request.body)
        data = request.POST.get("content")
        print(data)
        data = {
            "content":str(data)
        }
        # data = json.loads(data)


        # data = {
        #     "content":''
        # }

        aa = models.test.objects.create(**data)

        return HttpResponse(aa)
    else:
        return HttpResponse("失败")


    # 姜楠部分
    # 插入详情
    # Create your views here.
def show(request):
    # 帖子id
    pass
    # try:
    #     pid = request.GET.get('postid')
    #     print(pid)
    #     contents = models.content.objects.filter(postid=1).values()
    #     contents = list(contents)
    #     for item in contents:
    #         item["time"] = item["time"].strftime("%Y-%m-%d")
    #     contents = json.dumps(contents)
    #     return HttpResponse(contents)
    # except Exception as ex:
    #     print(ex)
    #     return JsonResponse({"code":"500"})

def edit(request):
    pass
    # if request.method=="POST":
    #     try:
    #         dcontent=request.POST.get("content")
    #         djcontent = {
    #             "html":dcontent
    #         }
    #         print(111)
    #         jdata = json.dumps(djcontent)
    #         f = open('file1.json','w')
    #         f.write(jdata)
    #         f.close()
    #         return JsonResponse({"code": 200})
    #     except Exception as ex:
    #         return JsonResponse({"code": 404})
    # elif request.method == "GET":
    #     return JsonResponse({"code": 100})

def insertdetail(request):
    if request.method == "GET":
        data = models.test.objects.filter(id="2").values('content')
        # data = str(data)
        # data = list(data)
        # temdata = data[0]['content']
        # print(type(temdata))
        return HttpResponse(json.dumps(list(data), ensure_ascii=False))
        # return JsonResponse({"content":temdata},json_dumps_params={'ensure_ascii':False})
    if request.method == 'POST':

        data = json.loads(request.body, strict=False)
        # data =request.body
        aa = models.test.objects.create(**data)
        # print(type(data.decode('utf-8')))
        # content1 = {
        #     "content" : data
        # }
        # print(json.dumps(data.decode()))
        print(aa)
        return HttpResponse('')
    else:
        return HttpResponse("失败")
def addtext(request):
    pass