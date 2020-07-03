import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import UserModel


def index(request):
    return render(request,'index.html')


def upload(request):
    if request.method =='GET':
        return render(request,'upload.html')
    elif request.method =='POST':
        icon = request.FILES.get('icon')
        print(icon)
        print(type(icon))
        file = request.FILES.get('file', '')
        with open('./static/img/1.gif','wb') as f:
            for part in icon.chunks():
                f.write(part)
                f.flush()

    return HttpResponse('文件上传成功')


def imgfield(request):
    if request.method == 'GET':
        return render(request, 'img_field.html')
    elif request.method =='POST':
        username = request.POST.get('username')
        icon = request.FILES.get('icon')
        user = UserModel()
        user.u_name = username
        user.u_icon = icon
        user.save()

        return HttpResponse('保存成功 %d' % user.id)




    # return None


def mine(request):
    username = request.GET.get('username')
    user = UserModel.objects.get(u_name=username)

    print('/static/upload/'+user.u_icon.url)

    data= {
        'username':username,
        'icon_url':'/static/upload/'+user.u_icon.url
    }

    #return HttpResponse('个人信息')
    return render(request,'mine.html',context=data)