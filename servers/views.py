from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from servers.models import Server


class ServerList(ListView):
    model = Server


class ServerCreate(CreateView):
    model = Server
    success_url = reverse_lazy('server_list')
    fields = ['name', 'ip', 'order']


class ServerUpdate(UpdateView):
    model = Server
    success_url = reverse_lazy('server_list')
    fields = ['name', 'ip', 'order']


class ServerDelete(DeleteView):
    model = Server
    success_url = reverse_lazy('server_list')