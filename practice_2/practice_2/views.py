from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib import messages

def registerUser(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'form':form}
            messages.error(request,"Refill the form")
            return render(request,'registration/signup.html',context)
    form = RegistrationForm()
    context={'form':form}
    return render(request,'registration/signup.html',context)

def home(request):
    return render(request,'home.html')