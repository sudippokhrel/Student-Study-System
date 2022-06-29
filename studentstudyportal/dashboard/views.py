from django.shortcuts import render

#creating views here
def home(request):
    return render(request,'dashboard/home.html')
