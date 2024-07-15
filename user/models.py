from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



class User2(AbstractUser):
    cedula = models.CharField (max_length=30, verbose_name='Cedula',unique=True)
    tel_celular = models.CharField(max_length=100, default='', verbose_name='Num. Cedular',unique=True)
    direccion = models.CharField(max_length=200, verbose_name='Direccion')
    foto = models.ImageField(upload_to='avatar',verbose_name='Foto',blank=True)
    tipo_usu = [('G', 'General - Manager'),
               ('C', 'Coordinador/Supervisor'),
                ('F', 'Financial'),
                ('H', 'Home Team - Contractor'),
               ]
    tipousuario = models.CharField(max_length=1, choices=tipo_usu, default='G')

    class Meta:
        verbose_name = 'UsuariosFer'
        verbose_name_plural = 'UsuariosFer'
