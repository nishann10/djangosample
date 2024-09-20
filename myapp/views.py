from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def my(request):
    a={"name":"nishan"}
    return render(request,"my.html",a)
def fun1(request):
    return HttpResponse("hello world")
def mypage(request):
    b={"name":"arun"}
    return render(request,"if.html",b)
def forloop(request):
    # a={"fruits":["apple","banana","cherry"]}
    # return render(request,"forloop.html",a)    

     
     a=[
         {"name":"apple","price":20,"quantity":10},
         {"name":"banana","price":30,"quantity":20},
         {"name":"cherry","price":40,"quantity":30},
     ]
 
     return render(request,"forloop.html",{"fruits":a}) 

def userget(request):
    user1=user.objects.all()
    return render(request,"modelsget.html",{'a':user1})
def userpost(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        place=request.POST.get('place')
        userdet=user()
        userdet.user_id=id
        userdet.user_name=name
        userdet.user_place=place
        userdet.save()
        return redirect("aa")
    return render(request,"modelspost.html")    
def userupdate(request,id):
    user1=user.objects.filter(user_id=id)
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        place=request.POST.get('place')
        userdet=user()
        userdet.user_id=id
        userdet.user_name=name
        userdet.user_place=place
        userdet.save()
        return redirect('aa')
    return render(request,"userupdate.html",{'a':user1})
def userdelete(request,id):
    user1=user.objects.get(user_id=id)
    user1.delete()
    return redirect("aa")
        