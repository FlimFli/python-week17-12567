from email import message
from urllib import request

from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = loader.get_template('My first.html')
    return HttpResponse(template.render())

def members_data(requeat):
    var = {"first name":"Flim","last_name":"Fli"}
    mData = Members()
    mData.firstname = "Name"
    mData.lastname = "Surename"
    try:
        mData.save()
        massage.success(request,"Complete!")
    except:
        massage.success(request,"Try again!")
    finally:
        return render(request,)
        