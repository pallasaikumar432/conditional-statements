from django.shortcuts import render

# Create your views here.
def sai(request):
    a=12
    b=int(input('enter b value'))

    return render(request,'sai.html')