from django.contrib.auth.models import User
from django.db import models

# Create your models here.


from django.db import models
from datetime import datetime

# Create your models here.
from user.models import User2


class Franja(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Franja')
    hora_inicial = models.IntegerField(verbose_name='Hora Inicial')
    hora_final = models.IntegerField(verbose_name='Hora Final')
    fecha_creacion = models.DateField(default=datetime.now)
    estados = [('A', 'Activo'),
               ('C', 'Cancelado')
               ]
    estado = models.CharField(max_length=1, choices=estados, default='A')

    def __str__(self):
        txt = "{0} {1} {2} {3} {4} {5}"
        return txt.format('Nombre : ', self.nombre,'--- Inicia a las : ',self.hora_inicial,'--- Termina a las : ',self.hora_final)

    class Meta:
        verbose_name = 'Franja de Intervenciòn'
        verbose_name_plural = 'Franja de Intervenciòn'
        ordering = ['hora_inicial']

class Cosec(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Cosec')
    fecha_creacion = models.DateField(default=datetime.now)
    estados = [('A', 'Activo'),
               ('C', 'Cancelado')
               ]
    estado = models.CharField(max_length=1, choices=estados, default='A')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Cosec'
        verbose_name_plural = 'Cosec'
        ordering = ['nombre']

class Punto(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Punto')
    estados = [('A', 'Activo'),
               ('C', 'Cancelado')
               ]
    estado = models.CharField(max_length=1, choices=estados, default='A')
    fecha_creacion = models.DateField(default=datetime.now)

    def __str__(self):
        txt = "{0} "
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Punto'
        verbose_name_plural = 'Puntos'
        ordering = ['nombre']


class Localidad(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Localidad')
    fecha_creacion = models.DateField(default=datetime.now)
    estados = [('A', 'Activo'),
               ('C', 'Cancelado')
               ]
    estado = models.CharField(max_length=1, choices=estados, default='A')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        ordering = ['nombre']


class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Tipo Usuario')
    fecha_creacion = models.DateField(default=datetime.now)
    estados = [('A', 'Activo'),
               ('C', 'Cancelado')
               ]
    estado = models.CharField(max_length=1, choices=estados, default='A')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Tipo de Usuario'
        verbose_name_plural = 'Tipo de Usuario'
        ordering = ['nombre']



class Turnos(models.Model):
    cosec = models.ForeignKey(Cosec, on_delete=models.PROTECT, null=False, blank=False, default='')
    usuarioturno = models.ForeignKey(User2, on_delete=models.PROTECT, null=False, blank=False, default='')
    localidad = models.ForeignKey(Localidad,on_delete=models.PROTECT, null=False, blank=False, default='')
    franja = models.ForeignKey(Franja,on_delete=models.PROTECT, null=False, blank=False, default='')
    punto = models.ForeignKey(Punto,on_delete=models.PROTECT, null=False, blank=False, default='')
    creado_por = models.CharField(max_length=100,verbose_name='Creado por', default='')
    fechadelturno = models.DateField(default='')
    asistio = models.BooleanField(default=False)
    ingreso_a_las = models.DateTimeField(default='',null=True,blank=True)
    salio_a_las = models.DateTimeField(default='',null=True,blank=True)

    def __str__(self):
        txt = "{0} {1} {2} {3} {4}"
        return txt.format(self.cosec, self.usuarioturno, self.localidad, self.franja, self.creado_por)

    class Meta:
        verbose_name = 'Turnos'
        verbose_name_plural = 'Turnos'
        ordering = ['cosec','franja']

