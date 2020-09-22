from django.shortcuts import render
from userapp.forms import userregisterform
from django.http import HttpResponse

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = userregisterform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('registered')
        else:
            form = userregisterform()

    else:
        form = userregisterform()
        dict={'form': form}
        return render(request,'userapp/register.html',dict)

def profile(request):
    return HttpResponse('logged in')
