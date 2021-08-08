from .models import *
from django.forms import ModelForm, TextInput, DateInput, CheckboxInput


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["name", "date_birth", "active"]
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
                   'date_birth': DateInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату рождения'}),
                   'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active_boolean'})
                   }
