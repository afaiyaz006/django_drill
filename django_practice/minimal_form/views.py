from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseNotFound
from .basicForms import BasicForm
from .models import SampleFormData
def infoViewer(request):
    datas=SampleFormData.objects.all()
    

    return render(request,'display_data.html',{'datas':datas.values()})

def homeView(request):
    return render(request,template_name="home.html")

def viewForm(request):
    if request.method=="POST":
        form=BasicForm(request.POST)
        if form.is_valid():
            full_name=form.cleaned_data['firstname']+" "+form.cleaned_data['lastname']
            gender_id=form.cleaned_data['gender']
            gender=""
            if(gender_id==1):
                gender="Male"
            else:
                gender="Female"
            email=form.cleaned_data['email_adress']
            phone_number=form.cleaned_data['phone_number']
            store=SampleFormData(fullname=full_name,gender=gender,email=email,phone_number=phone_number)
            store.save()
            print("Submission Successfull")
    form=BasicForm()
    return render(request,'basic_form.html',{'form':form})