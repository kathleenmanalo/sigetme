from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from datetime import datetime
from Modulos.Cobranza.models import Cartera, Pagos3, Gastos, Observaciones, CarteraTotales, Colocaciones, \
    Cartera_Resumen, IngresosVarios, Pagos_historicos, OtrosIngresos
from Modulos.guardog_wh.models import   *


class DashboardView2(TemplateView):
    template_name = 'dashboard.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = OrderContractor.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def pay_per_mes(self):
        data = []
        valor = 0
        try:
            ano = datetime.now().year
            for mes in range(1, 13):
                resul = Liquidacion.objects.filter(fecha_liquidacion__month=mes,fecha_liquidacion__year=ano)
                for items in resul:
                    valor = valor + items.valor_pagado
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def cerradas_por_mes(self):
        data = []
        valor = 0
        try:
            ano = datetime.now().year
            for mes in range(1, 13):
                resul = OrderContractor.objects.filter(Created_date__month=mes,Created_date__year=ano,closed='Y')
                for items in resul:
                    valor = valor + 1
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def abiertas_por_mes(self):
        data = []
        valor = 0
        try:
            ano = datetime.now().year
            for mes in range(1, 13):
                resul = OrderContractor.objects.filter(Created_date__month=mes,Created_date__year=ano,closed='N')
                for items in resul:
                    valor = valor + 1
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def total_por_mes(self):
        data = []
        valor = 0
        try:
            ano = datetime.now().year
            for mes in range(1, 13):
                resul = OrderContractor.objects.filter(Created_date__month=mes,Created_date__year=ano)
                for items in resul:
                    valor = valor + 1
                data.append(valor)
                valor = 0
        except:
            pass
        return data
    #

    def home_team(self):
        data = []
        valor = 0
        try:
            ano = datetime.now().year
            for mes in range(1, 13):
                resul = OrderContractor.objects.filter(Created_date__month=mes,Created_date__year=ano,Contractor=1)
                for items in resul:
                    valor = valor + 1
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def in_house(self):
        data = []
        valor = 0
        try:
            ano = datetime.now().year
            for mes in range(1, 13):
                resul = OrderContractor.objects.filter(Created_date__month=mes,Created_date__year=ano,Contractor=2)
                for items in resul:
                    valor = valor + 1
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def famorfe(self):
        data = []
        valor = 0
        try:
            ano = datetime.now().year
            for mes in range(1, 13):
                resul = OrderContractor.objects.filter(Created_date__month=mes,Created_date__year=ano,Contractor=3)
                for items in resul:
                    valor = valor + 1
                data.append(valor)
                valor = 0
        except:
            pass
        return data
    #

    def pagos_x_mes(self):
        data = []
        valor = 0
        try:
            ano = datetime.now().year
            for mes in range(1, 13):
                resul = Pagos3.objects.filter(fecha_pago__month=mes, fecha_pago__year=ano,observacion__contains='PAGO')
                for items in resul:
                    valor = items.valor_pagado + valor
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def gestion_Yamile(self):
        data = []
        try:
            ano = datetime.now().year
            for mes in range(1, 13):
                todo = Observaciones.objects.filter(fecha_visita__month=mes, fecha_visita__year=ano, asesor=2).count()
                data.append(todo)
        except:
            pass
        return data

    def gestion_Milton(self):
        data = []
        try :
            ano = datetime.now().year
            for mes in range (1,13):
                todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=3).count()
                data.append(todo)
        except:
            pass
        return data

    def gestion_Fdo(self):
        data = []
        try :
            ano = datetime.now().year
            for mes in range (1,13):
                todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=1).count()
                data.append(todo)
        except:
            pass
        return data

    def gestion_Osw(self):
        data = []
        try :
            ano = datetime.now().year
            for mes in range (1,13):
                todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=4).count()
                data.append(todo)
        except:
            pass
        return data

    def gestion_Mario(self):
        data = []
        try :
            ano = datetime.now().year
            for mes in range (1,13):
                todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=5).count()
                data.append(todo)
        except:
            pass
        return data

    def gestion_Abogado(self):
        data = []
        try :
            ano = datetime.now().year
            for mes in range (1,13):
                todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=7).count()
                data.append(todo)
        except:
            pass
        return data

    def gestion_Malka(self):
        data = []
        try :
            ano = datetime.now().year
            for mes in range (1,13):
                todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=18).count()
                data.append(todo)
        except:
            pass
        return data

    def gestion_Yamile_2(self):
        data = []
        try :
            ano = datetime.now().year
            mes = datetime.now().month
            for dia in range (1,31):
                todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=2,fecha_visita__day=dia).count()
                data.append(todo)
        except:
            pass
        return data

    def gestion_Malka_2(self):
        data = []
        try :
            ano = datetime.now().year
            mes = datetime.now().month
            for dia in range (1,31):
                todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=18,fecha_visita__day=dia).count()
                data.append(todo)
        except:
            pass
        return data

    def tot_Yamile_Mes(self):
        data = []
        try :
            ano = datetime.now().year
            mes = datetime.now().month
            todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=2).count()
            data.append(todo)
        except:
            pass
        return todo

    def gestion_Milton_2(self):
        data = []
        try :
            ano = datetime.now().year
            mes = datetime.now().month
            for dia in range (1,31):
                todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=3,fecha_visita__day=dia).count()
                data.append(todo)
        except:
            pass
        return data

    def tot_Milton_Mes(self):
        data = []
        try :
            ano = datetime.now().year
            mes = datetime.now().month
            todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=3).count()
            data.append(todo)
        except:
            pass
        return todo

    def gestion_Osw_2(self):
        data = []
        try:
            ano = datetime.now().year
            mes = datetime.now().month
            for dia in range(1, 31):
                todo = Observaciones.objects.filter(fecha_visita__month=mes, fecha_visita__year=ano, asesor=4,
                                                    fecha_visita__day=dia).count()
                data.append(todo)
        except:
            pass
        return data

    def tot_Osw_Mes(self):
        data = []
        try :
            ano = datetime.now().year
            mes = datetime.now().month
            todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=4).count()
            data.append(todo)
        except:
            pass
        return todo

    def gestion_Fer_2(self):
        data = []
        try:
            ano = datetime.now().year
            mes = datetime.now().month
            for dia in range(1, 31):
                todo = Observaciones.objects.filter(fecha_visita__month=mes, fecha_visita__year=ano, asesor=1,
                                                    fecha_visita__day=dia).count()
                data.append(todo)
        except:
            pass
        return data

    def tot_Fer_Mes(self):
        data = []
        try :
            ano = datetime.now().year
            mes = datetime.now().month
            todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=1).count()
            data.append(todo)
        except:
            pass
        return todo


    def gestion_Mario_2(self):
        data = []
        try:
            ano = datetime.now().year
            mes = datetime.now().month
            for dia in range(1, 31):
                todo = Observaciones.objects.filter(fecha_visita__month=mes, fecha_visita__year=ano, asesor=5,
                                                    fecha_visita__day=dia).count()
                data.append(todo)
        except:
            pass
        return data

    def tot_Mario_Mes(self):
        data = []
        try :
            ano = datetime.now().year
            mes = datetime.now().month
            todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=5).count()
            data.append(todo)
        except:
            pass
        return todo

    def gestion_Abogado_2(self):
        data = []
        try:
            ano = datetime.now().year
            mes = datetime.now().month
            for dia in range(1, 31):
                todo = Observaciones.objects.filter(fecha_visita__month=mes, fecha_visita__year=ano, asesor=7,
                                                    fecha_visita__day=dia).count()
                data.append(todo)
        except:
            pass
        return data

    def tot_Abogado_Mes(self):
        data = []
        try :
            ano = datetime.now().year
            mes = datetime.now().month
            todo = Observaciones.objects.filter(fecha_visita__month=mes,fecha_visita__year=ano,asesor=7).count()
            data.append(todo)
        except:
            pass
        return todo

    def gestion_Promedio(self):
        data = []
        try:
            ano = datetime.now().year
            mes = datetime.now().month
            for dia in range(1, 31):
                todo = Observaciones.objects.filter(fecha_visita__month=mes, fecha_visita__year=ano, fecha_visita__day=dia).count()
                todo = todo/6
                data.append(todo)
        except:
            pass
        return data


    def tot_Promedio_x_dia(self):
        data = []
        valor = 0
        try:
            ano = datetime.now().year
            mes = datetime.now().month
            dia = datetime.now().day + 1
            resul = Pagos3.objects.filter(fecha_pago__month=mes, fecha_pago__year=ano,observacion__contains='PAGO')
            for items in resul:
                valor = items.valor_pagado + valor
            promedio_dia = valor/(dia-1)
            for dia in range(1, dia-1):
                 data.append(promedio_dia)
        except:
            pass
        return data

    def tot_Pagos_x_dia(self):
        data = []
        valor = 0

        try:
            ano = datetime.now().year
            mes = datetime.now().month
            for dia in range(1, 31):
                resul = Pagos3.objects.filter(fecha_pago__month=mes, fecha_pago__year=ano, fecha_pago__day=dia,observacion__contains='PAGO')
                for items in resul:
                        valor = items.valor_pagado + valor
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def gastos_mes(self):
        data = []
        valor = 0
        try:
            ano = datetime.now().year
            for mes in range(1, 13):
                resul = Gastos.objects.filter(fecha_gasto__month=mes, fecha_gasto__year=ano)
                for items in resul:
                    valor = items.valor + valor
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def cartera_totales_mes(self):
        data = []
        valor = 0
        try:
            mes = datetime.now().month
            for mes_index in range(1, 13):
                if mes_index == mes:
                    resul = Cartera.objects.filter(estado='A').aggregate(Sum('saldo_total'))
                    a = resul['saldo_total__sum']
                    data.append(a)
                else:
                    data.append(0)

        except:
            pass
        return data

    def colocaciones_mes(self):
        data = []
        valor = 0
        try:
            ano = datetime.now().year
            for mes in range(1, 13):
                resul = Cartera_Resumen.objects.filter(fecha_colocacion__month=mes,fecha_colocacion__year=ano)
                for items in resul:
                    valor = items.valor + valor
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def comision_mipyme(self):
        data = []
        valor = 0
        try:
            ano = datetime.now().year
            for mes in range(1, 13):
                resul = IngresosVarios.objects.filter(fecha__month=mes,fecha__year=ano,concepto="Comision")
                for items in resul:
                    valor = items.valor_base + valor
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def estudio_credito(self):
        data = []
        valor = 0
        try:
            ano = datetime.now().year
            for mes in range(1, 13):
                resul = IngresosVarios.objects.filter(fecha__month=mes,fecha__year=ano,concepto="Estudio Credito")
                for items in resul:
                    valor = items.valor_base + valor
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def tot_Pagos_2017(self):
        data = []
        valor = 0

        try:
            ano = 2017
            for mes in range(1, 13):
                resul = Pagos3.objects.filter(fecha_pago__month=mes, fecha_pago__year=ano,observacion__contains='PAGO')
                for items in resul:
                        valor = items.valor_pagado + valor
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def tot_Pagos_2018(self):
        data = []
        valor = 0

        try:
            ano = 2018
            for mes in range(1, 13):
                resul = Pagos3.objects.filter(fecha_pago__month=mes, fecha_pago__year=ano,observacion__contains='PAGO')
                for items in resul:
                        valor = items.valor_pagado + valor
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def tot_Pagos_2019(self):
        data = []
        valor = 0

        try:
            ano = 2019
            for mes in range(1, 13):
                resul = Pagos3.objects.filter(fecha_pago__month=mes, fecha_pago__year=ano,observacion__contains='PAGO')
                for items in resul:
                        valor = items.valor_pagado + valor
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def tot_Pagos_2020(self):
        data = []
        valor = 0

        try:
            ano = 2020
            for mes in range(1, 13):
                resul = Pagos3.objects.filter(fecha_pago__month=mes, fecha_pago__year=ano,observacion__contains='PAGO')
                for items in resul:
                        valor = items.valor_pagado + valor
                data.append(valor)
                valor = 0
        except:
            pass
        return data

    def tot_Pagos_2021(self):
        data = []
        valor = 0

        try:
            ano = 2021
            for mes in range(1, 13):
                if mes >=1:
                    resul = Pagos3.objects.filter(fecha_pago__month=mes, fecha_pago__year=ano,observacion__contains='PAGO')
                    for items in resul:
                        valor = items.valor_pagado + valor
                    data.append(valor)
                valor = 0
        except:
            pass
        return data

    def tot_Pagos_2022(self):
        data = []
        valor = 0

        try:
            ano = 2022
            for mes in range(1, 13):
                if mes >=1:
                    resul = Pagos3.objects.filter(fecha_pago__month=mes, fecha_pago__year=ano,observacion__contains='PAGO')
                    for items in resul:
                        valor = items.valor_pagado + valor
                    data.append(valor)
                valor = 0
        except:
            pass
        return data

    def get_tipo_Normalidad(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(calificacion__in=('C','D','E'),estado__in=('A','F'),estado_juridicos__in=('N')).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def Normalidad_Abogados_x(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(estado__in=('A','F'),estado_juridicos__in=('N'),asesor__in=(7,8)).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def Pendiente_Abogados_x(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(estado__in=('A','F'),estado_juridicos__in=('P'),asesor__in=(7,8)).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def Bienes_Abogados_x(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(estado__in=('A','F'),estado_juridicos__in=('R'),asesor__in=(7,8)).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def Acuerdo_Abogados_x(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(estado__in=('A','F'),estado_juridicos__in=('A'),asesor__in=(7,8)).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def Embargo_Abogados_x(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(estado__in=('A','F'),estado_juridicos__in=('E'),asesor__in=(7,8)).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def Demanda_Abogados_x(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(estado__in=('A','F'),estado_juridicos__in=('D'),asesor__in=(7,8)).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def Ilocalizable_Abogados_x(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(estado__in=('A','F'),estado_juridicos__in=('I'),asesor__in=(7,8)).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def Fallo_Abogados_x(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(estado__in=('A','F'),estado_juridicos__in=('F'),asesor__in=(7,8)).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def Desest_Abogados_x(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(estado__in=('A','F'),estado_juridicos__in=('T'),asesor__in=(7,8)).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def get_tipo_Pendiente(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(calificacion__in=('C','D','E'),estado__in=('A','F'),estado_juridicos__in=('P')).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a=0
                    data.append(a)
        except:
            pass
        return data

    def get_tipo_Revision(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(calificacion__in=('C','D','E'),estado__in=('A','F'),estado_juridicos__in=('R')).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def get_tipo_Acuerdo(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(calificacion__in=('C','D','E'),estado__in=('A','F'),estado_juridicos__in=('A')).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def get_tipo_Embargado(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(calificacion__in=('C','D','E'),estado__in=('A','F'),estado_juridicos__in=('E')).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def get_tipo_Demandado(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(calificacion__in=('C','D','E'),estado__in=('A','F'),estado_juridicos__in=('D')).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def get_tipo_Ilocalizable(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(calificacion__in=('C','D','E'),estado__in=('A','F'),estado_juridicos__in=('I')).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def get_tipo_Fallado(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(calificacion__in=('C','D','E'),estado__in=('A','F'),estado_juridicos__in=('F')).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def get_tipo_Desestimiento(self):
        data = []
        try :
                Total_A = Cartera.objects.filter(calificacion__in=('C','D','E'),estado__in=('A','F'),estado_juridicos__in=('T')).aggregate(Sum('saldo_capital'))
                # print (Total_A['saldo_total__sum'])
                # print(Total_Cartera['saldo_total__sum'])
                a= Total_A['saldo_capital__sum']
                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def get_Interes_Recaudado(self):
        data = []
        try :
            ano = datetime.now().year
            for mes in range(1, 13):
                Total_A = Pagos3.objects.filter(fecha_pago__year=ano,fecha_pago__month=mes,observacion__contains='PAGO').aggregate(Sum('valorp_interes_cte'))
                Total_B = Pagos3.objects.filter(fecha_pago__year=ano, fecha_pago__month=mes,observacion__contains='PAGO').aggregate(
                    Sum('valorp_interes_mora'))
                a= Total_A['valorp_interes_cte__sum']
                b = Total_B['valorp_interes_mora__sum']

                if (a):
                    if (b):
                        a=a+b
                        data.append(a)
                    else:
                        data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def get_Capital_Recaudado(self):
        data = []
        try :
            ano = datetime.now().year
            for mes in range(1, 13):
                Total_A = Pagos3.objects.filter(fecha_pago__year=ano,fecha_pago__month=mes,observacion__contains='PAGO').aggregate(Sum('valorp_capital'))

                a= Total_A['valorp_capital__sum']


                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def get_CIFIN_Recaudado(self):
        data = []
        try :
            ano = datetime.now().year
            for mes in range(1, 13):
                Total_A = OtrosIngresos.objects.filter(fecha__year=ano,fecha__month=mes,concepto=20).aggregate(Sum('valor'))

                a= Total_A['valor__sum']


                if (a):
                    data.append(a)
                else:
                    a = 0
                    data.append(a)
        except:
            pass
        return data

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Dashboard '
        context['panel'] = 'Panel de Administrador'
        context['entidad'] = 'DashBoard'

        context['Pagos_por_mes'] =self.pagos_x_mes()
        context['Obs_Yamile'] = self.gestion_Yamile()
        context['Obs_Milton'] = self.gestion_Milton()
        context['Obs_Fdo'] = self.gestion_Fdo()
        context['Obs_Osw'] = self.gestion_Osw()
        context['Obs_Mario'] = self.gestion_Mario()
        context['Obs_Abogado'] = self.gestion_Abogado()
        context['Obs_Malka'] = self.gestion_Malka()
        context['Obs_Malka_2'] = self.gestion_Malka_2()
        context['Obs_Yamile_2'] = self.gestion_Yamile_2()
        context['Obs_Milton_2'] = self.gestion_Milton_2()
        context['Obs_Osw_2'] = self.gestion_Osw_2()
        context['Obs_Fer_2'] = self.gestion_Fer_2()
        context['Obs_Mario_2'] = self.gestion_Mario_2()
        context['Obs_Abogado_2'] = self.gestion_Abogado_2()
        context['Promedio'] = self.gestion_Promedio()
        context['tot_Yamile_mes'] =  self.tot_Yamile_Mes()
        context['tot_Milton_mes'] = self.tot_Milton_Mes()
        context['tot_Osw_mes'] = self.tot_Osw_Mes()
        context['tot_Fer_mes'] = self.tot_Fer_Mes()
        context['tot_Mario_mes'] = self.tot_Mario_Mes()
        context['tot_Abogado_mes'] = self.tot_Abogado_Mes()
        context['Pagos_por_dia'] = self.tot_Pagos_x_dia()
        context['Promedio_por_dia'] = self.tot_Promedio_x_dia()
        context['Gastos_Mensuales'] = self.gastos_mes()
        context['CarteraTotalMes'] = self.cartera_totales_mes()
        context['Colocaciones'] = self.colocaciones_mes()
        context['ComisionMiPyme'] = self.comision_mipyme()
        context['EstudiodeCredito'] = self.estudio_credito()
        #
        context['Pagos_2017'] = self.tot_Pagos_2017()
        context['Pagos_2018'] = self.tot_Pagos_2018()
        context['Pagos_2019'] = self.tot_Pagos_2019()
        context['Pagos_2020'] = self.tot_Pagos_2020()
        context['Pagos_2021'] = self.tot_Pagos_2021()
        context['Pagos_2022'] = self.tot_Pagos_2022()
        #
        context['Normalidad'] = self.get_tipo_Normalidad()
        context['Pendiente_Tramite'] = self.get_tipo_Pendiente()
        context['Revision_Bienes'] = self.get_tipo_Revision()
        context['Acuerdo'] = self.get_tipo_Acuerdo()
        context['Embargado'] = self.get_tipo_Embargado()
        context['Demandado'] = self.get_tipo_Demandado()
        context['Ilocalizable'] = self.get_tipo_Ilocalizable()
        context['Fallado'] = self.get_tipo_Fallado()
        context['Desestimiento'] = self.get_tipo_Desestimiento()
        #
        context['Normalidad_Abogados'] = self.Normalidad_Abogados_x()
        context['Pendiente_Abogados'] = self.Pendiente_Abogados_x()
        context['Bienes_Abogados'] = self.Bienes_Abogados_x()
        context['Acuerdo_Abogados'] = self.Acuerdo_Abogados_x()
        context['Embargo_Abogados'] = self.Embargo_Abogados_x()
        context['Demanda_Abogados'] = self.Demanda_Abogados_x()
        context['Ilocalizable_Abogados'] = self.Ilocalizable_Abogados_x()
        context['Fallo_Abogados'] = self.Fallo_Abogados_x()
        context['Desest_Abogados'] = self.Desest_Abogados_x()
        #
        context['Capital_Recaudado']= self.get_Capital_Recaudado()
        context['Interes_Recaudado'] = self.get_Interes_Recaudado()
        context['Cifin_Recaudado'] = self.get_CIFIN_Recaudado()
        #
        context['Abiertas_x_Mes'] = self.abiertas_por_mes()
        context['Cerradas_x_Mes'] = self.cerradas_por_mes()
        context['Total_x_Mes'] = self.total_por_mes()

        context['Home_Team'] = self.home_team()
        context['In_House'] = self.in_house()
        context['Famorfe'] = self.famorfe()
        context['Payment_per_mes'] = self.pay_per_mes()
        #
        return context
