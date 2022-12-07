from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Patients
from django.urls import reverse
# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))

def book(request):
    name = request.POST['name']
    contactno = request.POST['contactno']
    age = request.POST['age']
    reason = request.POST['reason']
    patient = Patients(name=name, contactno=contactno, age=age, reason=reason)
    patient.save()
    return HttpResponseRedirect(reverse(index))

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({},request))

def auth_admin(request):
    admin_detail = {"username" :"admin",
                    "password":"root123"}
    input_username , input_password = request.POST['username'],request.POST['password']
    if (input_username == admin_detail["username"]) and (input_password == admin_detail["password"]):
        template = loader.get_template("view.html")
        patients = Patients.objects.all().values()
        context = {"patients":patients}
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponseRedirect(reverse('loginpage'))