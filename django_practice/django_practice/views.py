from django.shortcuts import render

def showPage(request):
    return render(request,"site_nav.html")
