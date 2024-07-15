from django.db import models
from datetime import datetime,timedelta
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
            DateField, DateTimeField, IntegerField, TimeField, Transform,
        )

# Create your models here.
#He cambiado este archivo para ir mejorandolo--

def fecha_plus_30():
    fecha = datetime.now() + timedelta(days=30)
    return fecha

def fecha_plus_2():
    fecha = datetime.now() + timedelta(days=730)
    return fecha



class Ciudades(models.Model):
    nombre = models.CharField (max_length=60,unique=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Ciudades'
        verbose_name_plural = 'Ciudades'
        ordering = ['id']

class Nacionalidades(models.Model):
    nombre = models.CharField (max_length=60,unique=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Nacionalidades'
        verbose_name_plural = 'Nacionalidades'
        ordering = ['id']


class Destino(models.Model):
    nombre = models.CharField (max_length=60,unique=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Destinación'
        verbose_name_plural = 'Destinación'
        ordering = ['id']

class Actividades(models.Model):
    nombre = models.CharField (max_length=60,unique=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Actividades'
        verbose_name_plural = 'Actividades'
        ordering = ['id']


class Profesiones(models.Model):
    nombre = models.CharField (max_length=60,unique=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Profesiones'
        verbose_name_plural = 'Profesiones'
        ordering = ['id']


class Nivel_Estudio(models.Model):
    nombre = models.CharField (max_length=60,unique=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Nivel_Estudio'
        verbose_name_plural = 'Nivel_Estudio'
        ordering = ['id']

class Eps(models.Model):
    nombre = models.CharField (max_length=60,unique=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Eps'
        verbose_name_plural = 'Eps'
        ordering = ['id']


class Asesores(models.Model):
    nombre = models.CharField (max_length=100)
    estados = [ ('A','Activo'),
                    ('C','Cancelado')
                ]
    estado = models.CharField(max_length=1,choices=estados,default='A')

    def __str__(self):
        txt = "{0} - {1}"
        return txt.format(self.nombre, self.estado)

    class Meta:
        verbose_name = 'Asesores'
        verbose_name_plural = 'Asesores'
        ordering = ['nombre']

class Fases(models.Model):
    codigo = models.CharField (max_length=3,primary_key=True)
    nombre_fase = models.CharField (max_length=50,default='')
    responsable = models.ForeignKey(Asesores,on_delete=models.PROTECT,null=False, blank=False,default='')
    codigo_fase_siguiente = models.CharField (max_length=3,default='')

    def __str__(self):
        txt = "{0} - {1} - Fase Siguiente {2} "
        return txt.format(self.codigo, self.nombre_fase,self.codigo_fase_siguiente)

    class Meta:
        verbose_name = 'Fases'
        verbose_name_plural = 'Fases'
        ordering = ['codigo']


class Sectores(models.Model):
    nombre = models.CharField (max_length=60,unique=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sector'
        ordering = ['id']



class Clientes(models.Model):
    cedula = models.CharField (max_length=30,primary_key=True)
    apellidos = models.CharField (max_length=200,default='')
    nombres = models.CharField (max_length=200,default='')
    fecha_nacimiento = models.DateField(default=datetime.now)
    sexos = [ ('M','Masculino'),
                    ('F','Femenino')
                ]
    sexo     = models.CharField (max_length=1,choices=sexos,default='F')
    estadoci = [('S', 'Soltero'),
             ('C', 'Casado'),('V', 'Viudo'),('D', 'Divorciado')
             ]
    estado_civil = models.CharField(max_length=1, choices=estadoci, default='S')
    nacionalidad = models.ForeignKey(Nacionalidades,on_delete=models.PROTECT,null=False, blank=False,default='')
    ciudad_nacimiento = models.ForeignKey(Ciudades,on_delete=models.PROTECT,null=True, blank=True,default='')
    edad = models.IntegerField(default=0)
    tel_fijo     = models.CharField (max_length=100,default='')
    tel_celular  = models.CharField (max_length=100,default='')
    direccion_of   = models.CharField (max_length=200,default='')
    direccion_red  = models.CharField (max_length=200,default='')
    barrio  = models.CharField (max_length=200,default='')
    email = models.EmailField(unique=False, blank=True, null=True,default='')
    actividad = models.ForeignKey(Actividades,on_delete=models.PROTECT,null=False, blank=False,default='')
    nivel_estudio =  models.ForeignKey(Nivel_Estudio,on_delete=models.PROTECT,null=True, blank=True,default='')
    sector = models.ForeignKey(Sectores, on_delete=models.PROTECT, null=True, blank=True, default='')
    profesion =  models.ForeignKey(Profesiones,on_delete=models.PROTECT,null=True, blank=True,default='')
    propia = [ ('S','Si'),
                    ('N','No')
                ]
    vivienda_propia     = models.CharField (max_length=1,choices=propia,default='S')
    estratos = [ ('1','1'),
                    ('2','2'), ('3','3'),('4','4'),('5','5')
                ]
    estrato     = models.CharField (max_length=1,choices=estratos,default='2')
    total_ingresos = models.IntegerField(default=0)
    total_egresos = models.IntegerField(default=0)
    personas_cargo = models.IntegerField(default=1)
    eps =  models.ForeignKey(Eps,on_delete=models.PROTECT,null=False, blank=False,default='')
    nom_ref_1 = models.CharField (max_length=100,default='')
    tel_ref_1 = models.CharField (max_length=50,default='')
    dir_ref_1 = models.CharField (max_length=200,default='')
    nom_ref_2 = models.CharField (max_length=100,default='')
    tel_ref_2 = models.CharField (max_length=50,default='')
    dir_ref_2 = models.CharField (max_length=200,default='')
    nom_ref_3 = models.CharField (max_length=100,default='')
    tel_ref_3 = models.CharField (max_length=50,default='')
    dir_ref_3 = models.CharField (max_length=200,default='')
    score_cifin = models.IntegerField(null=False, blank=False,default=0)
    score_datacredito = models.IntegerField(null=False, blank=False,default=0)
    score_otro = models.IntegerField(null=False, blank=False,default=0)
    fecha_update = models.DateField(default=datetime.now)
    envio_estado_credito = models.BooleanField(default=False)
    envio_promociones = models.BooleanField(default=False)
    envio_cumple = models.BooleanField(default=False)
    envio_correo = models.EmailField(blank=False,default='')


    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.apellidos, self.nombres)

    class Meta:
        verbose_name = 'Clientes'
        verbose_name_plural = 'Clientes'
        ordering = ['apellidos']

class Cartera_Gestiones(models.Model):
    pagare = models.IntegerField(primary_key=True)
    tot_gestiones = models.IntegerField(default=0)

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.pagare, self.tot_gestiones)

    class Meta:
        verbose_name = 'Gestiones por Pagare'
        verbose_name_plural = 'Gestiones por Pagare'
        ordering = ['pagare']

class Cartera(models.Model):
    pagare = models.IntegerField(primary_key=True)
    operacion        = models.IntegerField (default=0)
    cedula           = models.ForeignKey(Clientes,on_delete=models.PROTECT,null=False, blank=False)
    fecha_desembolso = models.DateField(default=datetime.now)
    fecha_ult_pago   = models.DateField(default=datetime.now)
    fecha_prox_pago  = models.DateField(default=datetime.now)
    saldo_capital    = models.IntegerField(default=0)
    saldo_total      = models.IntegerField(default=0)
    plazo  = models.IntegerField(default=0)
    valor_cuota      = models.IntegerField(default=0)
    cuotas_mora      = models.IntegerField(default=0)
    cuotas_pendientes = models.IntegerField(default=0)
    dias_mora        = models.IntegerField(default=0)
    valor_mora       = models.IntegerField(default=0)
    calif = [ ('A','A'),
                    ('B','B'), ('C','C'),('D','D'),('E','E')
                ]
    calificacion     = models.CharField (max_length=1,choices=calif,default='A')
    saldo_para_normalizar = models.IntegerField(default=0)
    ciudad           = models.ForeignKey(Ciudades,on_delete=models.PROTECT,null=True, blank=True)
    asesor           = models.ForeignKey(Asesores,on_delete=models.PROTECT,null=True, blank=True)
    estados = [ ('A','Activo'),
           ('C','Cancelado')
          ]
    estado = models.CharField(max_length=1,choices=estados,default='A')
    fecha_update =  models.DateField(default=datetime.now)
    tot_gestiones = models.IntegerField(default=0,null=True)
    valor_solicitado = models.IntegerField(default=0,null=True)
    valor_desembolsado = models.IntegerField(default=1,null=True)
    fecha_ult_causacion = models.DateField(default=datetime.now)
    fase_c = [('A', 'Administrativo'),
               ('J', 'Juridico')
               ]
    fase_de_cobro = models.CharField(max_length=1,choices=fase_c,default='A')
    cant_msg_2 = models.IntegerField(default=0,null=True)
    cant_msg_3 = models.IntegerField(default=0, null=True)
    cant_msg_4 = models.IntegerField(default=0, null=True)
    cant_msg_5 = models.IntegerField(default=0, null=True)
    # tasas
    tasa_cte_ea = models.FloatField(max_length=5,default=51)
    tasa_cte_em = models.FloatField(max_length=5,default=3.55)
    tasa_mora_ea = models.FloatField(max_length=5,default=55)
    tasa_mora_em = models.FloatField(max_length=5,default=3.72)
    estados_j = [('P', 'Pendiente de Tramite'), ('R', 'Revisando Bienes'),('A', 'Acuerdo de Pago'),('E', 'Embargado'),('D', 'Demanda Presentada'),
                 ('I', 'Ilocalizable'),('F', 'Fallo a Favor'),('T', 'Desestimiento Tácito'),('N', 'Normalidad en Pagos')
               ]
    estado_juridicos = models.CharField(max_length=1, choices=estados_j, default='N')


    def __str__ (self):
     txt = "Cliente {0} - Num Credito {1}"
     return txt.format(self.cedula, self.operacion)

    class Meta:
        verbose_name = 'Cartera'
        verbose_name_plural = 'Carteras'
        ordering = ['cedula']


class Tipificaciones(models.Model):
    nombre = models.CharField (max_length=60,unique=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Tipificaciones'
        verbose_name_plural = 'Tipificaciones'
        ordering = ['id']


class Observaciones(models.Model):
    observacion = models.CharField (max_length=200,null=False, blank=False)
    fecha_visita    = models.DateField(default=datetime.now,null=False, blank=False)
    fecha_siguiente = models.DateField(default=datetime.now,null=False, blank=False)
    asesor = models.ForeignKey(Asesores,null=False,on_delete=models.PROTECT,default='')
    credito = models.ForeignKey(Cartera,null=False,on_delete=models.PROTECT)
    Tipificacion = models.ForeignKey(Tipificaciones,null=False,on_delete=models.PROTECT,default='')
    Valor_pagado = models.IntegerField(default=0)
    gest = [('S', 'Gestionado'),('N', 'NO Gestionado') ]
    gestionados = models.CharField(max_length=1, choices=gest, default='N')

    def __str__(self):
        txt = "Credito {0} - Asesor que Visitó : {1} - Fecha de Visita : {2} - Observación : {3} - Fecha Próxima : {4} - Gestionado : {5}"
        return txt.format(self.credito, self.asesor, self.fecha_visita.strftime('%d-%m-%Y'),self.observacion,self.fecha_siguiente.strftime('%d-%m-%Y'),self.gestionados)

    class Meta:
        verbose_name = 'Observaciones'
        verbose_name_plural = 'Observaciones'
        ordering = ['-fecha_siguiente']


class Cobros(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False,default='Nombre Cobro')
    valor = models.FloatField(max_length=5,default=0)
    fijo = [('F', 'Valor Fijo'),
             ('S','Sobre el Saldo')
             ]
    fijo_var =  models.CharField(max_length=1, choices=fijo, default='F')
    tipoc = [('U', 'Unico - Al Comienzo'),
             ('M', 'Mensual')
             ]
    tipo_cobro = models.CharField(max_length=1, choices=tipoc, default='U')
    fecha_update = models.DateField(default=datetime.now)

    def __str__(self):
        txt = "Nombre del Cobro : {0} - Valor : {1} - Tipo de Cobro : {2} - Fecha_Upd : {3}"
        return txt.format(self.nombre,self.valor,self.tipo_cobro,self.fecha_update.strftime('%d-%m-%Y'))

    class Meta:
        verbose_name = 'Cobros'
        verbose_name_plural = 'Cobros'
        ordering = ['id']


class Tasa_Corriente(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False,default='Tasa Corriente x')
    tasa = models.FloatField(max_length=5,default=57.2)
    fecha_update = models.DateField(default=datetime.now)

    def __str__(self):
        txt = "Nombre : {0} - Tasa {1} - Fecha Upd {2}"
        return txt.format(self.nombre,self.tasa,self.fecha_update.strftime('%d-%m-%Y'))

    class Meta:
        verbose_name = 'Tasa_Corriente'
        verbose_name_plural = 'Tasa_Corriente'
        ordering = ['id']


class Tasa_Mora(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False,default='Tasa Mora x')
    tasa = models.FloatField(max_length=5, default=50.2)
    fecha_update = models.DateField(default=datetime.now)

    def __str__(self):
        txt = "Nombre : {0} - Tasa {1} - Fecha Upd {2}"
        return txt.format(self.nombre, self.tasa, self.fecha_update.strftime('%d-%m-%Y'))

    class Meta:
        verbose_name = 'Tasa_Mora'
        verbose_name_plural = 'Tasa_Mora'


class Productos(models.Model):
    nombre =  models.CharField (max_length=200,null=False, blank=False)
    tasa_corriente = models.FloatField(default=0)
    tasa_mora = models.FloatField(default=0)
    fecha_update = models.DateField(default=datetime.now)
    estadol = [('A', 'Activo'),
             ('I', 'Inactivo')
             ]
    estado = models.CharField(max_length=1, choices=estadol, default='A')
    comision = models.FloatField(default=7)
    seguro = models.FloatField(default=2)
    estudio = models.IntegerField(default=35000)
    centrales = models.IntegerField(default=5000)
    monto_min = models.IntegerField(default=500000)
    monto_max = models.IntegerField(default=5000000)
    Observaciones = models.CharField (max_length=200,default='')

    def __str__(self):
        txt = "Nombre : {0} -  Tasa Cte : {1} - Tasa Mora : {2} -  fecha Update : {3} "
        return txt.format(self.nombre, self.tasa_corriente, self.tasa_mora,self.fecha_update.strftime('%d-%m-%Y'))


    class Meta:
        verbose_name = 'Productos'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class IngresosVarios(models.Model):
    cedula = models.ForeignKey(Clientes, on_delete=models.PROTECT, null=False, blank=False)
    concepto = models.CharField(max_length=100,default='')
    valor_base = models.FloatField()
    valor_iva = models.FloatField()
    fecha = models.DateField(default=datetime.now)
    pagare = models.ForeignKey(Cartera,null=False,on_delete=models.PROTECT)



class Asesorias(models.Model):
    cedula = models.ForeignKey(Clientes, on_delete=models.PROTECT, null=False, blank=False)
    valor = models.IntegerField (blank=False,default='', validators=[
            MaxValueValidator(30000000),
            MinValueValidator(500000)])
    plazo = models.IntegerField (blank=False,default='', validators=[
            MaxValueValidator(80),
            MinValueValidator(6)])
    producto = models.ForeignKey(Productos, on_delete=models.PROTECT, null=False, blank=False,default='')
    fase = models.ForeignKey(Fases, on_delete=models.PROTECT, null=False, blank=False,default=1)
    observa_asesoria = models.CharField(max_length=400,default='')
    observa_analisis = models.CharField(max_length=400, default='')
    observa_aprobacion = models.CharField(max_length=400, default='')
    estado_a = [('A', 'Aprobado'),
               ('R', 'Rechazado')]
    estado = models.CharField(max_length=1, choices=estado_a, default='A')
    fecha_asesoria = models.DateField(default=datetime.now)
    analizado = models.BooleanField(default=False)
    aprobado = models.BooleanField(default=False)
    requiere_codeudor = models.BooleanField(default=False)
    retanqueo = models.BooleanField(default=False)
    desembolsado = models.BooleanField(default=False,verbose_name='Impresión y Firma de Pagaré :')
    en_firme = models.BooleanField(default=False)
    fecha_primer_pago = models.DateField(default='')
    ciudad_radicacion = models.ForeignKey(Ciudades, on_delete=models.PROTECT, default=1)
    asesor = models.ForeignKey(Asesores, on_delete=models.PROTECT,default=1)
    pagare_ant = models.IntegerField(default=0)
    periodo_sgte = models.IntegerField(default=1)
    cuotas_pendientes = models.IntegerField(default=0)
    cuotas_corrimiento = models.IntegerField(default=0)
    credito_pandemia = models.IntegerField(default=0)
    medios = [('C', 'Cheque'),
                ('E', 'Efectivo')]
    medio_desembolso = models.CharField(max_length=1, choices=medios, default='C')
    valor_de_retanqueo = models.IntegerField(default=0)


    def __str__(self):
        txt = "Cedula : {0} -  valor : {1} - plazo : {2} -  Producto : {3} - fecha Asesoria : {4} - fase {5}"
        return txt.format(self.cedula, self.valor, self.plazo,self.producto,self.fecha_asesoria.strftime('%d-%m-%Y'),self.fase)


    class Meta:
        verbose_name = 'Asesorias'
        verbose_name_plural = 'Asesorias'
        ordering = ['id']

#
class PrestamosIn(models.Model):
    cedula = models.ForeignKey(Clientes, on_delete=models.PROTECT, null=False, blank=False)
    valor = models.IntegerField (blank=False,default='', validators=[
            MaxValueValidator(30000000),
            MinValueValidator(100000)])
    estado_a = [('A', 'Activo'),
               ('P', 'Pagado')]
    estado = models.CharField(max_length=1, choices=estado_a, default='A')
    fecha_consignacion = models.DateField(default=datetime.now)
    fecha_devolucion = models.DateField(default='')
    ciudad_radicacion = models.ForeignKey(Ciudades, on_delete=models.PROTECT, default=1)
    medios = [('C', 'Cheque'),
                ('E', 'Efectivo')]
    medio_consignacion = models.CharField(max_length=1, choices=medios, default='C')
    tasa_mensual = models.FloatField(max_length=3, default=1)

    def __str__(self):
        txt = "Cedula : {0} -  valor : {1} - fecha Consignacion : {2}"
        return txt.format(self.cedula, self.valor, self.fecha_consignacion)

    class Meta:
        verbose_name = 'Prestamistas'
        verbose_name_plural = 'Prestamistas'
        ordering = ['id']

#
class Plan_de_Pagos(models.Model):
    asesoria_num = models.ForeignKey(Asesorias,on_delete=models.PROTECT)
    periodo = models.IntegerField(default=0)
    valor_cuota =  models.FloatField()
    valor_interes = models.FloatField()
    valor_capital = models.FloatField()
    valor_saldo = models.FloatField()
    valor_seguro = models.FloatField()
    valor_comision = models.FloatField()
    valor_iva_comision = models.FloatField()
    fecha_de_pago = models.DateField(default=datetime.now)

    def __str__(self):
        txt = "id_Asesoria {0}  "
        return txt.format(self.asesoria_num)

    class Meta:
        verbose_name = 'Plan de Pagos'
        verbose_name_plural = 'Plan de Pagos'
        ordering = ['periodo']

class Plan_Cuotas(models.Model):
    pagare_num = models.ForeignKey(Cartera,null=False,on_delete=models.PROTECT)
    asesoria_num = models.ForeignKey(Asesorias,on_delete=models.PROTECT)
    periodo = models.IntegerField(default=0) # 1,2,3,4, corresponde a las cuotas en orden
    fecha_vencimiento = models.DateField(default=datetime.now) # fecha de cuando SE DEBE pagar la cuota
    fecha_de_pago = models.DateField(null=True, blank=True) # fecha cuando se pagó la cuota
    valor_capital = models.FloatField(default=0)
    valor_interes_cte = models.FloatField(default=0)
    valor_interes_mora = models.FloatField(default=0)
    valor_seguro = models.FloatField(default=0)
    valor_iva_seguro = models.FloatField(default=0)
    valor_comision = models.FloatField(default=0)
    valor_iva_comision = models.FloatField(default=0)
    valor_otros_cargos = models.FloatField(default=0)
    valor_iva_otros = models.FloatField(default=0)
    valor_a_pagar = models.FloatField(default=0)
    valor_tasa_aplicada = models.FloatField(default=0)
    valor_capital_proy = models.FloatField(default=0)

    def __str__(self):
        txt = "Pagare {0}  "
        return txt.format(self.pagare_num)

    class Meta:
        verbose_name = 'Plan de Pagos Real'
        verbose_name_plural = 'Plan de Pagos Real'
        ordering = ['pagare_num','periodo']

class Codeudores(models.Model):
    cedula_c = models.ForeignKey(Clientes, on_delete=models.PROTECT, null=True, blank=True,verbose_name='Cedula de Codeudor')
    pagare_num_c = models.IntegerField(default=0,verbose_name='Pagare No.')
    asesoria_num_c = models.IntegerField(primary_key=True,verbose_name='Asesoria No.')

    def __str__(self):
        txt = "Codeudor {0}  "
        return txt.format(self.cedula_c)

    class Meta:
        verbose_name = 'Codeudores'
        verbose_name_plural = 'Codeudores'
        ordering = ['asesoria_num_c']

class Retanqueos(models.Model):
    pagare = models.ForeignKey(Cartera,null=False,on_delete=models.PROTECT)
    fecha_recogida = models.DateField(null=True, blank=True)
    valor_recogido = models.FloatField(default=0)
    asesoria = models.ForeignKey(Asesorias,on_delete=models.PROTECT)

    def __str__(self):
        txt = "Pagare {0}  "
        return txt.format(self.valor_recogido)

    class Meta:
        verbose_name = 'Retanqueos'
        verbose_name_plural = 'Retanqueos'
        ordering = ['pagare']

class Plan_Cuotas_OnLine(models.Model):
    pagare_num = models.ForeignKey(Cartera,null=False,on_delete=models.PROTECT)
    asesoria_num = models.ForeignKey(Asesorias,on_delete=models.PROTECT)
    periodo = models.IntegerField(default=0) # 1,2,3,4, corresponde a las cuotas en orden
    fecha_vencimiento = models.DateField(default=datetime.now) # fecha de cuando SE DEBE pagar la cuota
    fecha_de_pago = models.DateField(null=True, blank=True) # fecha cuando se pagó la cuota
    valor_capital = models.FloatField(default=0)
    valor_interes_cte = models.FloatField(default=0)
    valor_interes_mora = models.FloatField(default=0)
    valor_seguro = models.FloatField(default=0)
    valor_iva_seguro = models.FloatField(default=0)
    valor_comision = models.FloatField(default=0)
    valor_iva_comision = models.FloatField(default=0)
    valor_otros_cargos = models.FloatField(default=0)
    valor_iva_otros = models.FloatField(default=0)
    valor_a_pagar = models.FloatField(default=0)
    valor_tasa_aplicada = models.FloatField(default=0)
    valor_capital_proy = models.FloatField(default=0)
    dia_de_mora = models.IntegerField(default=0)

    def __str__(self):
        txt = "Pagare {0}  "
        return txt.format(self.pagare_num)

    class Meta:
        verbose_name = 'Plan de Pagos en Linea'
        verbose_name_plural = 'Plan de Pagos en Linea'
        ordering = ['pagare_num','periodo']

class Soporte_Pagos(models.Model):
    pagare_num = models.ForeignKey(Cartera,null=False,on_delete=models.PROTECT)
    periodo = models.IntegerField(default=0) # 1,2,3,4, corresponde a las cuotas en orden
    campo_modificado = models.CharField(default='',max_length=50)
    fecha_pago = models.DateField(default=datetime.now) # fecha de cuando SE DEBE pagar la cuota
    valor_anterior = models.FloatField(default=0)
    valor_nuevo = models.FloatField(default=0)
    valor_global_pagado = models.FloatField(default=0)

    def __str__(self):
        txt = "Pagare {0}  "
        return txt.format(self.pagare_num)

    class Meta:
        verbose_name = 'Auditoria de Pagos'
        verbose_name_plural = 'Auditoria de Pagos'
        ordering = ['pagare_num','periodo']


class Cartera_Resumen(models.Model):
    pagare_num = models.ForeignKey(Cartera,null=False,on_delete=models.PROTECT)
    asesoria_num = models.ForeignKey(Asesorias,on_delete=models.PROTECT)
    fecha_colocacion = models.DateField(default=datetime.now)
    valor = models.FloatField(default=0)
    observacion = models.CharField (max_length=200,null=False, blank=False,default='')
    medio = models.CharField (max_length=1,default='C') #Cheque o Efectivo

    def __str__(self):
        txt = "Pagare {0}  "
        return txt.format(self.pagare_num)

    class Meta:
        verbose_name = 'Cartera_Resumen'
        verbose_name_plural = 'Cartera_Resumen'
        ordering = ['pagare_num']


class Pagos3(models.Model):
    pagare = models.ForeignKey(Cartera,null=False,on_delete=models.PROTECT)
    fecha_pago    = models.DateField(default=datetime.now,null=False, blank=False)
    valor_pagado = models.FloatField(default=0)
    observacion = models.CharField (max_length=200,null=False, blank=False,default='')
    valorp_capital = models.FloatField(default=0)
    valorp_interes_cte = models.FloatField(default=0)
    valorp_interes_mora = models.FloatField(default=0)
    valorp_seguro = models.FloatField(default=0)
    valorp_comision = models.FloatField(default=0)
    valorp_iva_comision = models.FloatField(default=0)
    usuario = models.CharField(max_length=20, default='')
    medio = [('B', 'Banco/Corresponsales'),
               ('O', 'Oficina')
               ]
    pagado_en = models.CharField(max_length=1, choices=medio, default='O')

    def __str__(self):
        txt = "Pagare : {0} -  valor : {1}  - fecha {2}"
        return txt.format(self.pag_are, self.valor_pagado,self.fecha_pago.strftime('%d-%m-%Y'))


    class Meta:
        verbose_name = 'Pagos'
        verbose_name_plural = 'Pagos'
        ordering = ['id']


#

class Pagos_historicos(models.Model):
    pagare_id = models.IntegerField(default=0)
    fecha_pago    = models.DateField(default=datetime.now,null=False, blank=False)
    valor_pagado = models.FloatField(default=0)
    observacion = models.CharField (max_length=200,null=False, blank=False,default='')
    valorp_capital = models.FloatField(default=0)
    valorp_interes_cte = models.FloatField(default=0)
    valorp_interes_mora = models.FloatField(default=0)
    valorp_seguro = models.FloatField(default=0)
    valorp_comision = models.FloatField(default=0)
    valorp_iva_comision = models.FloatField(default=0)
    usuario = models.CharField(max_length=20, default='')
    medio = [('B', 'Banco/Corresponsales'),
               ('O', 'Oficina')
               ]
    pagado_en = models.CharField(max_length=1, choices=medio, default='O')

    def __str__(self):
        txt = "Pagare : {0} -  valor : {1}  - fecha {2}"
        return txt.format(self.pag_are, self.valor_pagado,self.fecha_pago.strftime('%d-%m-%Y'))


    class Meta:
        verbose_name = 'Pagos'
        verbose_name_plural = 'Pagos'
        ordering = ['pagare_id']



#


class ConceptosGastos(models.Model):
    nombre = models.CharField (max_length=100,unique=True)
    tipox = [('G', 'Gasto'),
             ('I', 'Ingreso')
             ]
    tipo = models.CharField(max_length=1, choices=tipox, default='G')

    def __str__(self):
        txt = "Concepto : {0}  del Tipo : {1}"
        return txt.format(self.nombre,self.tipo)

    class Meta:
        verbose_name = 'Concepto'
        verbose_name_plural = 'Concepto'
        ordering = ['id']


class Gastos(models.Model):
    valor = models.IntegerField()
    concepto = models.ForeignKey(ConceptosGastos,on_delete=models.PROTECT)
    fecha_gasto = models.DateField(default=datetime.now)

    def __str__(self):
        txt = "concepto {0} valor {1} Fecha {2} "
        return txt.format(self.concepto,self.valor,self.fecha_gasto)

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
        ordering = ['-fecha_gasto']

class CarteraTotales(models.Model):
    valor = models.IntegerField()
    fecha_corte = models.DateField(default=datetime.now)

    def __str__(self):
        txt = "valor {0} Fecha {1} "
        return txt.format(self.valor,self.fecha_corte)

    class Meta:
        verbose_name = 'Cartera Totales'
        verbose_name_plural = 'Cartera Totales'
        ordering = ['-fecha_corte']

class Colocaciones(models.Model):
    valor = models.IntegerField()
    fecha_corte = models.DateField(default=datetime.now)

    def __str__(self):
        txt = "valor {0} Fecha {1} "
        return txt.format(self.valor,self.fecha_corte)

    class Meta:
        verbose_name = 'Colocaciones'
        verbose_name_plural = 'Colocaciones'
        ordering = ['-fecha_corte']

class Documentos(models.Model):
    asesoria_num = models.IntegerField(primary_key=True)
    fecha_update = models.DateField(default=datetime.now)
    cedula = models.BooleanField(default=False)
    autorizacion = models.BooleanField(default=False)
    resultado_cifin = models.BooleanField(default=False)
    resultado_data = models.BooleanField(default=False)
    facturas = models.BooleanField(default=False)
    recibos_servicios = models.BooleanField(default=False)
    camara_comercio = models.BooleanField(default=False)
    rut = models.BooleanField(default=False)
    fotos = models.BooleanField(default=False)
    certificacion_laboral = models.BooleanField(default=False)
    se_valido = models.BooleanField(default=False)
    observacion= models.CharField(max_length=400, default='')



    def __str__(self):
        txt = "Asesoria : {0} "
        return txt.format(self.asesoria_num)


    class Meta:
        verbose_name = 'Documentos Necesarios'
        verbose_name_plural = 'Documentos Necesarios'
        ordering = ['asesoria_num']

class Mensajeria(models.Model):
    numero = models.IntegerField(primary_key=True)
    mensaje = models.CharField(max_length=400, default='')

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.numero, self.mensaje)

    class Meta:
        verbose_name = 'Mensajes'
        verbose_name_plural = 'Mensajes'
        ordering = ['-numero']

class Auditoria_mensajes(models.Model):
    tel_celular = models.CharField (max_length=20,null=False, blank=False)
    fecha_mensaje   = models.DateField(default=datetime.now,null=False, blank=False)
    tipo_mensaje = models.IntegerField (null=False, blank=False)
    mensajes = models.CharField(max_length=200,default='')
    pagare = models.IntegerField(default=0)

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.tel_celular,self.mensajes)

    class Meta:
        verbose_name = 'Auditoria Mensajeria'
        verbose_name_plural = 'Auditoria Mensajeria'
        ordering = ['-fecha_mensaje']

class TratamientoFinanciero(models.Model):
    fecha = models.DateField(default=datetime.now,null=False, blank=False)
    interes_cte_causado = models.FloatField(default=0)
    interes_mora_causado = models.FloatField(default=0)
    seguro_causado = models.FloatField(default=0)
    comision_causada = models.FloatField(default=0)
    cartera_de_capital = models.FloatField(default=0)

    def __str__(self):
        txt = "Fecha : {0} -  Cartera : {1}  - Interes Cte{2}"
        return txt.format(self.fecha.strftime('%d-%m-%Y'), self.cartera_de_capital,self.interes_cte_causado)

    class Meta:
        verbose_name = 'Tratamiento Financiero'
        verbose_name_plural = 'Tratamiento Financiero'
        ordering = ['fecha']

class TablaCentrales(models.Model):
    cedula = models.ForeignKey(Clientes, on_delete=models.PROTECT, null=False, blank=False)
    fecha_desembolso = models.DateField(default=datetime.now)
    operacion = models.IntegerField()
    num_pagare = models.IntegerField(unique=True)
    num_cifin = models.CharField(max_length=20)
    num_datacredito = models.CharField(max_length=20)


    def __str__(self):
        txt = "Cedula : {0} -  operacion : {1} - pagare : {2}"
        return txt.format(self.cedula, self.operacion, self.pagare)


    class Meta:
        verbose_name = 'TablaCentrales'
        verbose_name_plural = 'TablaCentrales'
        ordering = ['id']

class OtrosIngresos(models.Model):
    concepto = models.ForeignKey(ConceptosGastos, on_delete=models.PROTECT)
    valor = models.FloatField()
    fecha = models.DateField(default=datetime.now)
    observacion= models.CharField(max_length=200, default='')
    medio = [('B', 'Banco/Corresponsales'),
             ('O', 'Oficina')
             ]
    pagado_en = models.CharField(max_length=1, choices=medio, default='O')


    def __str__(self):
        txt = "{0} {1} {2}"
        return txt.format(self.concepto, self.valor, self.fecha)


    class Meta:
        verbose_name = 'OtrosIngresos'
        verbose_name_plural = 'OtrosIngresos'
        ordering = ['id']

class ReporteCartera(models.Model):
    pagare = models.ForeignKey(Cartera,null=False,on_delete=models.PROTECT)
    fecha_vencimiento  = models.DateField(default=datetime.now)
    valor_a_pagar = models.FloatField(default=0)
    dias_de_mora = models.IntegerField(default=0)


    def __str__(self):
        txt = "Pagare : {0} -  valor : {1}  - fecha {2}"
        return txt.format(self.pagare, self.valor_a_pagar,self.fecha_vencimiento.strftime('%d-%m-%Y'))


    class Meta:
        verbose_name = 'ReporteCartera'
        verbose_name_plural = 'ReporteCartera'
        ordering = ['pagare']

class Tipo_Auxiliar(models.Model):
    nombre = models.CharField (max_length=100,unique=True)


    def __str__(self):
        txt = "Concepto : {0}  "
        return txt.format(self.nombre)

    class Meta:
        verbose_name = 'Tipo_Auxiliar'
        verbose_name_plural = 'Tipo_Auxiliar'
        ordering = ['id']


class LibroAuxiliar(models.Model):

    fecha = models.DateField(default=datetime.now)
    hora = models.CharField(max_length=200, default='')
    concepto = models.ForeignKey(Tipo_Auxiliar, on_delete=models.PROTECT)
    Observacion= models.CharField(max_length=200, default='')
    valor_cierre = models.FloatField(default=0)
    valor_adicionado = models.FloatField(default=0)
    medio = [('A', 'Activo'),
             ('I', 'Inactivo')
             ]
    estado = models.CharField(max_length=1, choices=medio, default='A')


    def __str__(self):
        txt = "{0} {1} {2}"
        return txt.format(self.concepto, self.valor, self.fecha)


    class Meta:
        verbose_name = 'libroAuxiliar'
        verbose_name_plural = 'LibroAuxiliar'
        ordering = ['id']


class Fecha_Cierre(models.Model):

    fecha_negocio = models.DateField(default=datetime.now)



    def __str__(self):
        txt = "{0} "
        return txt.format(self.fecha)


    class Meta:
        verbose_name = 'Fecha_Cierre'
        verbose_name_plural = 'Fecha_Cierre'
        ordering = ['id']

