from django.http import request, HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend, filters
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.views.generic import *

# localhost/clients/
# localhost/clients/?order_by=date_birth&direction=asc


class ClientListView(ListView):

        model = Client
        queryset = Client.objects.filter(active=True).order_by('name')
        template_name = 'main/home_page.html'
        context_object_name = 'clients'

        def Pagination(self, dict, value):
            paginator = Paginator(value, 3)
            page_num = dict.get('page', 1)
            page_obj = paginator.get_page(page_num)
            return page_obj, paginator

        def get(self, request, *args, **kwargs):
            clients = Client.objects.filter(active=True)
            dict = request.GET
            url_dir = "asc"
            paginator = self.Pagination(dict, clients)

            if 'search' in request.GET:
                clients = Client.objects.filter(active=True, name=dict.get('search'))
                if 'order_by' in request.GET and 'dir' in request.GET:
                    if request.GET['dir'] == "asc":
                        clients = Client.objects.filter(active=True, name=dict.get('search')).order_by(
                            dict.get('order_by'))
                        url_dir = "desc"
                        paginator = self.Pagination(dict, clients)
                        return render(request, 'main/search_client.html',
                                      context={'clients': clients, 'url_dir': url_dir,
                                               'form': ClientForm, 'search_': dict.get('search'), 'page_obj': paginator[0], 'paginator': paginator[1]})
                    elif request.GET['dir'] == "desc":
                        clients = Client.objects.filter(active=True, name=dict.get('search')).order_by(
                            '-' + dict.get('order_by'))
                        url_dir = "asc"
                        paginator = self.Pagination(dict, clients)
                        return render(request, 'main/search_client.html',
                                      context={'clients': clients, 'url_dir': url_dir,
                                               'form': ClientForm, 'search_': dict.get('search'),'page_obj': paginator[0], 'paginator': paginator[1]})
                paginator = self.Pagination(dict, clients)
                return render(request, 'main/search_client.html',
                              context={'clients': clients, 'url_dir': 'asc', 'search_': dict.get('search'),'page_obj': paginator[0], 'paginator': paginator[1]})
            else:
                if 'order_by' in request.GET and 'dir' in request.GET:
                    if request.GET['dir'] == "asc":
                        clients = Client.objects.filter(active=True).order_by(dict.get('order_by'))
                        url_dir = "desc"
                        paginator = self.Pagination(dict, clients)
                        return render(request, 'main/home_page.html',
                                      context={'clients': clients, 'url_dir': url_dir, 'form': ClientForm,'page_obj': paginator[0], 'paginator': paginator[1]})
                    elif request.GET['dir'] == "desc":
                        clients = Client.objects.filter(active=True).order_by('-' + dict.get('order_by'))
                        url_dir = "asc"
                        paginator = self.Pagination(dict, clients)
                        return render(request, 'main/home_page.html',
                                      context={'clients': clients, 'url_dir': url_dir, 'form': ClientForm,'page_obj': paginator[0], 'paginator': paginator[1]})
                else:
                    paginator = self.Pagination(dict, clients)
                    return render(request, 'main/home_page.html',
                                  context={'clients': clients, 'url_dir': url_dir, 'form': ClientForm,
                                           'page_obj': paginator[0], 'paginator': paginator[1]})


class ClientUpdateView(UpdateView):
    model = Client
    queryset = Client.objects.all()
    template_name = 'main/client_info_update.html'
    form_class = ClientForm
    pk_url_kwarg = 'client_id'


class ClientIsNotActive(UpdateView):
    model = Client
    queryset = Client.objects.all()
    template_name = 'main/client_is_not_active.html'
    pk_url_kwarg = 'client_id'
    fields = ["active"]

    def post(self, request, *args, **kwargs):
        client_id = kwargs['client_id']
        client = Client.objects.get(id=client_id)
        client.active = False
        client.save()
        return render(request, self.template_name, {client: 'client'})


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


class ClientDetailView(DetailView):
    model = Client
    template_name = 'main/definite_client.html'
    context_object_name = 'client'
    pk_url_kwarg = 'client_id'

# def check_definite_client(request, client_id):
#     client_information = Client.objects.get(id=client_id)
#     return render(request, 'main/definite_client.html', context={'title': client_information.name, 'client': client_information})


class ClientCreateView(CreateView):
    form_class = ClientForm
    model = Client
    template_name = 'main/registration.html'



    # def registration(request):
    #     error = ''
    #     if request.method == 'POST':
    #         form = ClientForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('main_url')
    #         else:
    #             error = 'Данные были заполнено не верно!'
    #
    #     form = ClientForm()
    #     return render(request, 'main/registration.html',
    #                   context={'title': 'Создать клиента', 'form': form, 'error': error})

class TestView(ListView):

    def get(self, request, *args, **kwargs):
        print(dir(request.GET))
        print(request.GET)
        print(request.GET['order_by'])
        print(request.GET['dir'])
        clients = Client.objects.filter(active=True)
        url_dir = ""
        if 'order_by' in request.GET and 'dir' in request.GET:
            if request.GET.get('dir') == "asc":
                clients = Client.objects.filter(active=True).order_by(request.GET['order_by'])
                url_dir = "desc"
                return render(request, 'main/test.html', context={'clients': clients, 'url_dir': url_dir})
            elif request.GET.get('dir') == "desc":
                clients = Client.objects.filter(active=True).order_by('-' + request.GET['order_by'])
                url_dir = "asc"
                return render(request, 'main/test.html', context={'clients': clients, 'url_dir': url_dir})
            else:
                clients = Client.objects.filter(active=True)

        return render(request, 'main/test.html', context={'clients': clients})
