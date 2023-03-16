from django.shortcuts import render

# Create your views here.
def loop(request):
    return render(request,'loop.html',context={'a':102,'b':105,'c':108})
def whilee(request):
    return render(request,'while.html',context={'name':'BASKAR'})