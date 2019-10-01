from django.shortcuts import render, HttpResponse


# Create your views here.
def personal(request):
    is_personal = request.user.groups.filter(name='Personal').exists()
    return render(request)

def home(request):
    return render(request, 'core/home.html')
