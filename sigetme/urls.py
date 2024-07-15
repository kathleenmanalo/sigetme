"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from Modulos.Cobranza.Vistas.Ciudades.views import CiudadesListView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     #path('Ciudades/listado', include('Modulos.Cobranza.urls'))
#     path('Ciudades/listado',CiudadesListView.as_view()),
# ]


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Modulos.homepage.views import IndexView
from Modulos.login.views import LoginFormView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('App/', include('Modulos.Cobranza.urls')),
    path('', IndexView.as_view(),name='index'),
    path('login/', include('Modulos.login.urls')),
   ]
