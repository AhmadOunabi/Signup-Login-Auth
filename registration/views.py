from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Registration
from faker import Faker
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

def user_faker(request):
    # User.objects.all().delete()
    # Registration.objects.all().delete()
    for i in range(1000):
        fake = Faker()
        username1=fake.name()
        list=username1.split()
        username=username1.replace(' ','_').lower()
        user=User.objects.create_user(
                                    username=username,
                                    first_name=list[0],
                                    last_name=list[1],
                                    email='{}@example.com'.format(username),
                                    password='password1234')
        registration=Registration.objects.create(user=user,
                                                name=username1,
                                                email='{}@example.com'.format(username),
                                                password='password1234')
    return HttpResponse('Users are Created successfully')


def charts_view(request):
    names_start_A=Registration.objects.filter(name__startswith='A').count()
    names_start_E=Registration.objects.filter(name__startswith='E').count()
    names_start_C=Registration.objects.filter(name__startswith='C').count()
    total_names=Registration.objects.all().count()
    
    ##user_list##
    orderd_users=User.objects.all().order_by('date_joined')[0:10]
    
    
    ratio_A= (names_start_A  / total_names)*100 if total_names > 0 else 0
    ratio_E= (names_start_E  / total_names)*100 if total_names > 0 else 0
    ratio_C= (names_start_C  / total_names)*100 if total_names > 0 else 0
    
    context={'ratio_A':ratio_A, 'ratio_E':ratio_E,'ratio_C':ratio_C,'orderd_users':orderd_users}
    
    return render(request,'registration/charts.html', context)


def charts_plotly(request):
    names_start_A=Registration.objects.filter(name__startswith='A').count()
    names_start_E=Registration.objects.filter(name__startswith='E').count()
    names_start_C=Registration.objects.filter(name__startswith='C').count()
    total_names=Registration.objects.all().count()
    
    ##user_list##
    #orderd_users=User.objects.all().order_by('date_joined')[0:10]
    
    ratio_A= (names_start_A  / total_names)*100 if total_names > 0 else 0
    ratio_E= (names_start_E  / total_names)*100 if total_names > 0 else 0
    ratio_C= (names_start_C  / total_names)*100 if total_names > 0 else 0
    
    context={'ratio_A':ratio_A, 'ratio_E':ratio_E,'ratio_C':ratio_C }
    
    return render(request,'registration/plotly.html', context)