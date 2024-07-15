from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView,UpdateView
from django.shortcuts import render
from Modulos.Cobranza.forms import *
from Modulos.Cobranza.mixins import ValidatePermissionRequiredMixin
from Modulos.guardog_wh.models import *
from django.views.generic import View
from xhtml2pdf import pisa
from django.db import connection
from django.conf import settings
from sigetme.settings import *




class CustomersListView(ListView):
    model = Customer
    template_name = 'Customers/list.html'
    reverse_lazy = 'Customers/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def get_queryset(self):
    #     lista = Asesorias.objects.filter(fase='1')
    #     return lista

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Customer.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Customers  Report'
        context['create_url'] = reverse_lazy('Cobranza:order_create')
        context['list_url'] = reverse_lazy('Cobranza:customers_list')
        context['entidad'] = 'Customers'
        context['Fase'] = 'Order'
        context['modo'] = 'Editar'
        return context

# Ord_Contrac_ListView
