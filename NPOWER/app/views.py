from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import dataForm

# Create your views here.

def register(request):
    submitted = False
    if request.method=="POST":
        form = dataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = dataForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'register.html', {"form":form, "submitted":submitted})

