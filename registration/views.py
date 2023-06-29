from django.shortcuts import render
from .forms import RegistrationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect , HttpResponse
from django. contrib.auth import login , logout , authenticate
from django.contrib.auth.hashers import make_password



def register(request):
    if request.method == 'POST':
        register_form=RegistrationForm(request.POST)
        if register_form.is_valid():
            user=register_form.save(commit=False)
            user.password=make_password(register_form.cleaned_data['password'])
            user.save()
    else:
        register_form=RegistrationForm()
    context={'register_form': register_form}
    return render(request, 'registration/registration.html', context)


def user_login(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user is not None:
            if user.is_active():
                login(request,user)
                return render(request, 'registration/home.html',{})
            else:
                return HttpResponse('Account is not active')
        else:
            return HttpResponse('Someone tried to login username:{} , password:{}'.format(user, password))
    else:
        return render(request, 'registration/login_user.html',{})
