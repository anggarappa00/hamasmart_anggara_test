from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
# Create your views here.

def home(request):
    list = Todo.objects.all()

    data = {
        'data': list
    }
    return render(request, 'home.html', data)

def create(request):
    if request.method == 'POST':
        forms = TodoForms(request.POST or None)

        if forms.is_valid():
            forms.save()
            return redirect('home')
    else:
        forms = TodoForms()

    return render(request, 'forms.html', {'forms':forms})

def update(request, id):
    data = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        forms = TodoForms(request.POST or None, instance=data)

        if forms.is_valid():
            forms.save()
            return redirect('home')
    else:
        forms = TodoForms(instance=data)

    return render(request, 'forms.html', {'forms':forms})

def delete(request, id):
    data = get_object_or_404(Todo, id=id)
    if data:
        data.delete()

    return redirect('home')