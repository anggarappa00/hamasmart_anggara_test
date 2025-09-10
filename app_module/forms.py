from .models import *
from django.db import models
from django import forms


class TodoForms(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name']
        labels = {
            'name': 'Nama'
        }

