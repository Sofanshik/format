from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.db.models import Q, Count


def main(request):
    return render(request, 'main/home_page.html')


def users_list(request):
    clients = Client.objects.order_by('id')

    # search_guery = request.GET.get('search', '')
    #
    # if search_guery:
    #     users = Client.objects.filter(Q(title__icontains=search_guery) | Q(text__icontains=search_guery))
    # else:
    #     users = Client.objects.all()
    #
    return render(request, 'main/all_users.html', context={'title': 'Все пользователи страницы', 'clients': clients})


def check_definite_client(request, client_id):
    client_information = Client.objects.get(id=client_id)
    return render(request, 'main/definite_client.html', context={'title': client_information.name, 'client': client_information})


def registration(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_url')
        else:
            error = 'Данные были заполнено не верно!'

    form = ClientForm()
    return render(request, 'main/registration.html', context={'title': 'Создать клиента', 'form': form, 'error': error})
