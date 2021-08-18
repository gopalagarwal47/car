from django.db.models.base import Model
from django.shortcuts import render, HttpResponse
from car.models import Contact
from car.models import Service
from hello.utils import message_mail


# Create your views here.
def index(request):
     return render(request, 'index.html')
    # return HttpResponse('this is homepage')

def about(request):
     return render(request, 'about.html')

def contact(request):
     if request.method == 'POST':
          name = request.POST['name']
          phone = request.POST['phone']
          address = request.POST['address']
          textarea = request.POST['textarea']
          print(name,phone,address,textarea)
          message_mail(name,phone,address,textarea)
          contact = Contact( name=name, phone=phone, address=address, textarea=textarea)
          contact.save()
     return render(request, 'contact.html')

def service(request):
     return render(request, 'service.html')

def gallery(request):
     return render(request, 'gallery.html')

def general(request):
     if request.method == 'POST':
          name = request.POST['name']
          phone = request.POST['phone']
          address = request.POST['address']
          company = request.POST.get('company',False)
          model= request.POST.get('model',False)
          print(name,phone,address,company,model)
          service=Service( name=name, phone=phone, address=address ,company=company, model=model)
          service.save()
     return render(request, 'general.html')  

def cardenting(request):
     if request.method == 'POST':
          name = request.POST['name']
          phone = request.POST['phone']
          address = request.POST['address']
          company = request.POST.get('company',False)
          model= request.POST.get('model',False)
          print(name,phone,address,company,model)
          service=Service( name=name, phone=phone, address=address ,company=company, model=model)
          service.save()
     return render(request, 'cardenting.html')

def carwashing(request):
     if request.method == 'POST':
          name = request.POST['name']
          phone = request.POST['phone']
          address = request.POST['address']
          company = request.POST.get('company',False)
          model= request.POST.get('model',False)
          print(name,phone,address,company,model)
          service=Service( name=name, phone=phone, address=address ,company=company, model=model)
          service.save()
     return render(request, 'carwashing.html')

def customrepairing(request):
     if request.method == 'POST':
          name = request.POST['name']
          phone = request.POST['phone']
          address = request.POST['address']
          company = request.POST.get('company',False)
          model= request.POST.get('model',False)
          print(name,phone,address,company,model)
          service=Service( name=name, phone=phone, address=address ,company=company, model=model)
          service.save()
     return render(request, 'customrepairing.html')  

def wheelcare(request):
     if request.method == 'POST':
          name = request.POST['name']
          phone = request.POST['phone']
          address = request.POST['address']
          company = request.POST.get('company',False)
          model= request.POST.get('model',False)
          print(name,phone,address,company,model)
          service=Service( name=name, phone=phone, address=address ,company=company, model=model)
          service.save()
     return render(request, 'wheelcare.html')  

def numberplating(request):
     if request.method == 'POST':
          name = request.POST['name']
          phone = request.POST['phone']
          address = request.POST['address']
          company = request.POST.get('company',False)
          model= request.POST.get('model',False)
          print(name,phone,address,company,model)
          service=Service( name=name, phone=phone, address=address ,company=company, model=model)
          service.save()
     return render(request, 'numberplating.html')    

def Privacypolicy(request):
     return render(request, 'Privacypolicy.html')       

def Termandcondition(request):
     return render(request, 'Termandcondition.html')                                                       