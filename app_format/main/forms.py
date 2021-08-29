from .models import *
from django.forms import ModelForm, TextInput, DateInput, CheckboxInput, EmailInput


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["name", "surname", "email", "date_birth"]
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
                   'surname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}),
                   'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'test@example.com'}),
                   'date_birth': DateInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату рождения'}),
                   }
