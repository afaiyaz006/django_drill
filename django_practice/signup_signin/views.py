from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

from django.shortcuts import redirect

def afterloginView(request):
    
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
  
    if user is not None:
        login(request,user)
        print(user.is_authenticated)
        print("loggedin")
        return render(request,"index.html")
    
    form=AuthenticationForm()
    return render(request,"registration/login.html",{'form':form,'error':'wrong username or password'})


def logoutView(request):
    logout(request)
    return render(request,"index.html")

def indexView(request):
    return render(request,'index.html')

def signupView(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            success_msg="Account "+user_name+" has been created."
            user=authenticate(request,username=user_name,password=password)
            if user is not None:
                login(request,user)
            return render(request,'index.html',{'user_created':success_msg})
        else:
            return render(request,'signup.html',{'form':form,'error_message':'User Not created'})
    form=UserCreationForm()
    return render(request,'signup.html',{'form':form})
