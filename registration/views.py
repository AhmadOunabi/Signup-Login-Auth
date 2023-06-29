from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        register_form=RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
    else:
        register_form=RegistrationForm()
    context={'register_form': register_form}
    return render(request, 'registration/registration.html', context)
