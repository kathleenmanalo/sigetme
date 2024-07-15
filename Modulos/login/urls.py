from Modulos.login.views import *
from django.urls import path

urlpatterns = [
       path('', LoginFormView.as_view(), name='login'),
       path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
   ]