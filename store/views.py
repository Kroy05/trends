from django.shortcuts import render
from .models import Store
from contact.models import contacts


def index(request):
    item_list=Store.objects.all()
    if request.method=="GET":
        st=request.GET.get('serac')
        if st!=None:
            item_list=Store.objects.filter(item_title__icontains=st)
    context={
        'item_list':item_list
    }

    return render(request,'store/index.html',context)


def detail(request,item_id):
    item=Store.objects.get(pk=item_id)
    context={
        'item':item,
    }

    return render(request,'store/detail.html',context)

def about(request):
    return render(request,'store/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        number=request.POST.get("number")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        en=contacts(name=name,number=number,mail=email,subject=subject,message=message)
        en.save()
    return render(request,'store/contact.html')


# Create your views here.
