from django.shortcuts import render
from .models import contacttable

# Create your views here.

def index(request):
    return render(request,"index.html")

def contactform(request):
    dict1={}
    try:
        m_name=request.POST['name']
        m_email=request.POST['email']
        m_sub=request.POST['subject']
        m_msg=request.POST['message']
        add=contacttable(name=m_name,email=m_email,subject=m_sub,message=m_msg)
        add.save()
        dict1['msg']="Message send Successfully"
        return render(request,"index.html",dict1)
    except Exception as e:
        print(e)
        dict1['msg']="Something is wrong!!"
        return render(request,"index.html",dict1)