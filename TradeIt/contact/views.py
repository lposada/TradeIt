from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
# Create your views here.
personal = Group(name = "Personal")

def check_admin(user):
    return user.groups.filter(name='Personal').exists()

@user_passes_test(check_admin)
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Suponemos que todo ha ido bien redireccionamos
            return redirect(reverse('contact')+"?ok")

    return render(request, 'contact/contact.html', {'form':contact_form})