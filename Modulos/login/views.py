from django.contrib.auth.views import *
from django.shortcuts import render, redirect


# Create your views here.

class LoginFormView(LoginView):
    template_name = 'login.html'

    # for g in request.user.groups.all():
    #     # print(g.name)
    #     if g.name == 'Cajero' or g.name == 'Administrador':
    #         es_Cajero = 1

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Cobranza:customers_list')
        return super().dispatch(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'iniciar Sesion'
        return context


