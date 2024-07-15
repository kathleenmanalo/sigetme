import os

from django.core.mail import EmailMultiAlternatives
from django.db.models import Max
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import timedelta
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from Modulos.Cobranza.forms import *
from Modulos.Cobranza.mixins import ValidatePermissionRequiredMixin
from Modulos.guardog_wh.models import *
from django.views.generic import View
from xhtml2pdf import pisa
from django.conf import settings
from django.template.loader import get_template

class Ord_Contrac_CreateView(ValidatePermissionRequiredMixin, CreateView):
    permission_required = 'Cobranza.add_order'
    url_redirect = reverse_lazy('Cobranza:list_order_contractor')
    model = OrderContractor
    form_class = OrderContractorForm
    template_name = 'Orders/create.html'  # Plantilla que usara mi CreateView o creador de formularios
    success_url = reverse_lazy('Cobranza:list_order_contractor')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

            context = super().get_context_data(**kwargs)
            context['titulo'] = 'Add Order'
            context['entidad'] = 'Orders'
            context['list_url'] = reverse_lazy('Cobranza:customers_list')
            context['action'] = 'nueva'
            return context


class Ord_Contrac_ListView(ListView):
    model = OrderContractor
    template_name = 'Contractors/list.html'
    reverse_lazy = 'Contractors/list.html'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detalle_orden = OrderContractorDetail.objects.all()
        context['titulo'] = 'Orders Contractor  Report'
        context['Detalle_Orden'] = detalle_orden
        context['create_url'] = reverse_lazy('Cobranza:create_order_contractor')
        context['list_url'] = reverse_lazy('Cobranza:list_order_contractor')
        context['entidad'] = 'Orders Contractor'
        context['Fase'] = 'Order'
        context['modo'] = 'Editar'
        return context

class Ord_Contrac_ListView_Open(ListView):
    model = OrderContractor
    template_name = 'Contractors/list.html'
    reverse_lazy = 'Contractors/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):

        if self.request.user.tipousuario == 'G':
            queryset = OrderContractor.objects.filter(closed='N')

        if self.request.user.tipousuario == 'H':
            queryset = OrderContractor.objects.filter(closed='N',Contractor_id=self.request.user.cedula)

        return queryset

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = OrderContractor.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detalle_orden = OrderContractorDetail.objects.all()
        context['titulo'] = 'Orders Contractor  Report - OPEN'
        context['Detalle_Orden'] = detalle_orden
        context['create_url'] = reverse_lazy('Cobranza:create_order_contractor')
        context['list_url'] = reverse_lazy('Cobranza:list_order_contractor')
        context['entidad'] = 'Orders Contractor'
        context['Fase'] = 'Order'
        context['modo'] = 'Editar'
        return context


class Ord_Contrac_ListView_Close(ListView):
    model = OrderContractor
    template_name = 'Contractors/list.html'
    reverse_lazy = 'Contractors/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.tipousuario == 'G':
            queryset = OrderContractor.objects.filter(closed='Y')
# FER
        if self.request.user.tipousuario == 'H':
            queryset = OrderContractor.objects.filter(closed='Y', Contractor_id=self.request.user.cedula)

        return queryset

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = OrderContractor.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detalle_orden = OrderContractorDetail.objects.all()
        context['titulo'] = 'Orders Contractor  Report - CLOSED'
        context['Detalle_Orden'] = detalle_orden
        context['create_url'] = reverse_lazy('Cobranza:create_order_contractor')
        context['list_url'] = reverse_lazy('Cobranza:list_order_contractor')
        context['entidad'] = 'Orders Contractor'
        context['Fase'] = 'Order'
        context['modo'] = 'Editar'
        return context

class Ord_Contrac_ListView_Entregado(ListView):
    model = OrderContractorDetail
    template_name = 'Contractors/list2.html'
    reverse_lazy = 'list_order_contractor_entregado'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):

       queryset = OrderContractorDetail.objects.filter(Qty_Delivery__gt=0,En_QuickB='N')
       return queryset

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         data = OrderContractor.objects.get(pk=request.POST['id']).toJSON()
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detalle_orden = OrderContractorDetail.objects.filter(Qty_Delivery__gt=0,En_QuickB='N')
        context['titulo'] = 'Assembly Log'
        context['Detalle_Orden'] = detalle_orden
        context['create_url'] = reverse_lazy('Cobranza:create_order_contractor')
        context['list_url'] = reverse_lazy('Cobranza:list_order_contractor')
        context['entidad'] = 'Orders Contractor'
        context['Fase'] = 'Order'
        context['modo'] = 'Editar'
        return context

class Ord_Contrac_ListView_EntrePlus(ListView):
    model = OrderContractorDetail
    template_name = 'Contractors/list2.html'
    reverse_lazy = 'list_order_contractor_entregado'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
       orden_afec = self.kwargs['id']
       queryset = OrderContractorDetail.objects.filter(Qty_Delivery__gt=0,En_QuickB='N',Orden_id=orden_afec)
       return queryset



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orden_afec = self.kwargs['id']
        detalle_orden = OrderContractorDetail.objects.filter(Qty_Delivery__gt=0,En_QuickB='N',Orden_id=orden_afec)
        context['titulo'] = 'Assembly Log'
        context['Detalle_Orden'] = detalle_orden
        context['create_url'] = reverse_lazy('Cobranza:create_order_contractor')
        context['list_url'] = reverse_lazy('Cobranza:list_order_contractor')
        context['entidad'] = 'Orders Contractor'
        context['Fase'] = 'Order'
        context['modo'] = 'Editar'
        return context


class AddItemToOrder_Cont(ValidatePermissionRequiredMixin,CreateView): # Esto es para crear un formulario de Asesorias
    permission_required = 'Cobranza.add_order'
    url_redirect = reverse_lazy('Cobranza:customers_list')
    model = OrderContractorDetail
    form_class = OrderDetails_Cont_Form
    template_name = 'Contractors/aditemtoorder_contractor.html'  # Plantilla que usara mi CreateView o creador de formularios
    success_url = reverse_lazy('Cobranza:customers_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Add Order'
        context['entidad'] = 'Orders'
        context['list_url'] = reverse_lazy('Cobranza:customers_list')
        context['action'] = 'nueva'
        return context



class Ord_Contrac_ListView_det(ListView):
    model = OrderContractorDetail
    template_name = 'Contractors/list_order_details.html'
    reverse_lazy = 'Contractors/list_order_details.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            print("1")
        if request.method == 'GET':
            print("2")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = OrderContractorDetail.objects.filter(Orden=self.kwargs['id'])
        return queryset

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = OrderContractorDetail.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = super().get_context_data(Orden=self.kwargs['id'])
        num = self.kwargs['id']
        estado_or = OrderContractor.objects.filter(id=str(num))
        for est in estado_or:
            est2 = est.closed
        context['titulo'] = 'Items for Order Num : ' + str(num)
        context['numero_orden'] = num
        context['Estado_Orden2'] = est2
        context['create_url'] = reverse_lazy('Cobranza:list_order_contractor')
        context['list_url'] = reverse_lazy('Cobranza:list_order_contractor')
        context['entidad'] = 'Order Details Contractor'
        context['Fase'] = 'Order'
        context['modo'] = 'Editar'
        return context


class OrderUpdateDetailView(ValidatePermissionRequiredMixin,UpdateView): # Esto es para crear un formulario de Asesorias
    permission_required = 'Cobranza.change_asesorias'
    url_redirect = reverse_lazy('Cobranza:list_order_contractor')
    model = OrderContractorDetail
    form_class = OrderDetails_Cont_Form_Upd
    template_name = 'Contractors/update_det.html'  # Plantilla que usara mi CreateView o creador de formularios
    success_url = reverse_lazy('Cobranza:list_order_contractor')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # asesoria = self.kwargs['pk']
        # list_asesoria = Order.objects.filter(id=asesoria)
        # for la in list_asesoria:
        #     es_retanqueo = la.retanqueo
        #     cedula_cliente = la.cedula_id
        #
        # es_retan = 0
        # if es_retanqueo:
        #     es_retan = 1

        context['titulo'] = 'Updating Item'
        context['entidad'] = 'Asesorias'
        context['list_url'] = reverse_lazy('Cobranza:customers_list')
        context['action'] = 'edit'
        return context


class print_full_order_cont(View):

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('Contractors/orden_completa.html')
            now = datetime.now() # asi asigno fecha del sistema para que se imprima en el pdf
            orden_master = OrderContractor.objects.filter(id=self.kwargs['order'])
            orden_detail2 = OrderContractorDetail.objects.filter(Orden_id=self.kwargs['order'])
            num_orden_pcpal = self.kwargs['order']

            for contratista in orden_master:
                cont_name = contratista.Contractor.Name
                inst_especiales = contratista.Special_Inst
                fecha_creacion = contratista.Created_date
            cuantos = 0
            for conteo_prod in orden_detail2:
                cuantos = cuantos + 1

            context = {
                'Orden_principal': orden_master,
                'Orden_datalle2': orden_detail2,
                'num_orden' : str(num_orden_pcpal),
                'nom_contratista': cont_name,
                'instrucciones':inst_especiales,
                'creada_el':fecha_creacion,
                'comp': {'name': 'SKY LINE USA', 'ruc': 'Phone : 888-800-8440',
                         'address': '4180 St Jhons PkWy , Sanford FL, 32771'},
                'icon': '{}{}'.format(settings.MEDIA_URL, 'LogoGuardog.png'),
                'icon2': '{}{}'.format(settings.MEDIA_URL, 'LogoGuardog22.png'),
                'fecha_a_imprimir' : now
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('Cobranza:list_order_contractor'))


class Aprobar_Orden(ListView): # Esto es para crear un formulario de Asesorias
    model = OrderContractor
    template_name = 'Contractors/list.html'  # Plantilla que usara
    success_url = reverse_lazy('Cobranza:list_order_contractor')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def get_queryset(self):
    #     lista = OrderContractor.objects.filter(closed='N')
    #     return lista

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        s = 0
        # Con esto accedo a los parametros de Kwargs
        for key, value in self.kwargs.items():
            # print(key, "=", value)
            s = value
            # context['plan'] = value
        # Aqui enviado el listado de unicamente lo que quiero mostrar
        OrderContractor.objects.filter(id=s).update(closed='Y')
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Order s Contractor'
        context['entidad'] = 'Asesorias'
        context['list_url'] = reverse_lazy('Cobranza:list_order_contractor_open')
        context['action'] = 'list'
        return context


class AddItemToOrder_Cont_V2(ValidatePermissionRequiredMixin,CreateView): # Esto es para crear un formulario de Asesorias
    permission_required = 'Cobranza.add_order'
    url_redirect = reverse_lazy('Cobranza:customers_list')
    model = OrderContractorDetail
    form_class = OrderDetails_Cont_Form_v2
    template_name = 'Contractors/add_item_order_contract2.html'  # Plantilla que usara mi CreateView o creador de formularios
    success_url = reverse_lazy('Cobranza:customers_list')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orden_principal = self.kwargs['id']
        detalle_orden = OrderContractorDetail.objects.filter(Orden_id=orden_principal)
        context['titulo'] = 'Adding Items to Order No : '
        context['orden_main'] = orden_principal
        context['entidad'] = 'Orders'
        context['list_url'] = reverse_lazy('Cobranza:customers_list')
        context['action'] = 'nueva'
        context['orden_al_detalle'] = detalle_orden
        return context


class producto_terminado(ListView): #
    model = OrderContractor
    template_name = 'Contractors/list.html'  # Plantilla que usara
    success_url = reverse_lazy('Cobranza:list_order_contractor_open')

    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            print('2')
        if request.method == 'GET':
            print('22')
            s = 0
            # Con esto accedo a los parametros de Kwargs
            for key, value in self.kwargs.items():
                # print(key, "=", value)
                s = value
                # context['plan'] = value
            # Aqui enviado el listado de unicamente lo que quiero mostrar
            cant = OrderContractorDetail.objects.filter(id=s)
            for cantid in cant:
                cant_req = cantid.Qty_Req
            OrderContractorDetail.objects.filter(id=s).update(Terminado='Y', fecha=datetime.now(),
                                                              Qty_Delivery=cant_req)
            # send_email2('ferortega1971@hotmail.com','Prueba2','Fer Ortega',1)
            for a in cant:
                orden_afectada = a.Orden_id

            request.path = ''
            request.path_info = ''
            return redirect('/App/OrderContractor/list_det/'+str(orden_afectada))

        return super().dispatch(request, *args, **kwargs)

    # def get_queryset(self):
    #     lista = OrderContractor.objects.filter(closed='N')
    #     return lista

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required()
def add_item3(request):
    print('Adding ITEM.....')
    datos = []
    if request.method == 'POST':
        orden_in = int(request.POST['orden2'])
        prod_in = int(request.POST['prod2'])
        qty_in = int(request.POST['qty2'])
        sellado_in = request.POST['sellado_v']
        barcode_in =request.POST['barcode_v']
        instrucc_in = request.POST['instrucc']
        Orden_Contractor_detail = OrderContractorDetail(Qty_Req=qty_in,Sellado=sellado_in,
                                                        Barcode=barcode_in,Orden_id=orden_in,
                                                        Product_id=prod_in,Special_Inst=instrucc_in,
                                                        Terminado='N',fecha=None,fecha_de_pago=None)
        Orden_Contractor_detail.save()
        print('Aqui acabe de grabar')
        datos.append(100)
        return JsonResponse({'Result': datos})
    else:
        return HttpResponse("Peticion no valida")


class OrderDeleteDetailView(ValidatePermissionRequiredMixin,DeleteView): # Esto es para crear un formulario de Asesorias
    permission_required = 'Cobranza.change_asesorias'
    url_redirect = reverse_lazy('Cobranza:list_order_contractor')
    model = OrderContractorDetail
    form_class = OrderDetails_Cont_Form_Upd
    template_name = 'Contractors/delete.html'  # Plantilla que usara mi CreateView o creador de formularios
    success_url = reverse_lazy('Cobranza:list_order_contractor')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # asesoria = self.kwargs['pk']
        # list_asesoria = Order.objects.filter(id=asesoria)
        # for la in list_asesoria:
        #     es_retanqueo = la.retanqueo
        #     cedula_cliente = la.cedula_id
        #
        # es_retan = 0
        # if es_retanqueo:
        #     es_retan = 1

        context['titulo'] = 'Deleting Item'
        context['entidad'] = 'Contractor Orders'
        context['list_url'] = reverse_lazy('Cobranza:customers_list')
        context['action'] = 'edit'
        return context


class Reporte_Inicial_Financiero(ListView):
    model = OrderContractorDetail
    template_name = 'Financial/report1.html'
    reverse_lazy =  reverse_lazy('Cobranza:list_order_contractor')

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detalle_orden = OrderContractorDetail.objects.filter(Terminado='Y',Pagado='N').order_by('Orden_id')
        context['titulo'] = 'Payment Process - Contractors'
        context['Detalle_Orden'] = detalle_orden
        context['create_url'] = reverse_lazy('Cobranza:generar_pagos2')
        context['list_url'] = reverse_lazy('Cobranza:list_order_contractor')
        context['entidad'] = 'Ready to Pay'
        context['Fase'] = 'Order'
        context['modo'] = 'Editar'
        return context


class Generar_Pagos2(ListView): #
    model = OrderContractor
    template_name = 'Contractors/list.html'  # Plantilla que usara
    success_url = reverse_lazy('Cobranza:list_order_contractor_open')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        num_max = Num_Liquidacion.objects.all().order_by('-Numero_Liq')[0]
        num_max2 = num_max.Numero_Liq + 1
        nueva_liq = Num_Liquidacion(Numero_Liq=num_max2,Contractor_id=99999)
        nueva_liq.save()
        num_liq = num_max2

        para_pagar = OrderContractorDetail.objects.filter(Terminado='Y',Pagado='N').order_by('Orden_id')
        OrderContractorDetail_Temp.objects.all().delete()
        for bb in para_pagar:
            OrderContractorDetail_Tempx = OrderContractorDetail_Temp(Qty_Req=bb.Qty_Req, Sellado=bb.Sellado,
                                                            Barcode=bb.Barcode, Orden_id=bb.Orden_id,
                                                            Product_id=bb.Product_id, Special_Inst=bb.Special_Inst,
                                                            Terminado=bb.Terminado, fecha=bb.fecha,
                                                            fecha_de_pago=bb.fecha_de_pago,Qty_Delivery=bb.Qty_Delivery,
                                                                     Contractor_id=bb.Orden.Contractor.id)
            OrderContractorDetail_Tempx.save()
            OrderContractorDetail.objects.filter(id=bb.id).update(Pagado='Y',fecha_de_pago=datetime.now())

        para_pagar2 = OrderContractorDetail_Temp.objects.filter(Terminado='Y', Pagado='N').order_by('Contractor_id')
        ciclo=1
        valor_nuevo = 0
        for cc in para_pagar2:

            if ciclo==1:
                aux_contractor=cc.Contractor_id
                if cc.Sellado == 'Y':
                    valor_nuevo = valor_nuevo + .01
                if cc.Barcode == 'Y':
                    valor_nuevo = valor_nuevo + .01

                valor_nuevo2 = cc.Qty_Delivery * (cc.Product.rate.valor + valor_nuevo)

                Listo = Liquidacion(Qty_Delivery=cc.Qty_Delivery,valor_unit=cc.Product.rate.valor,
                                    valor_pagado=valor_nuevo2,
                                    fecha_liquidacion=datetime.now(),Orden_id=cc.Orden_id,
                                    Product_id=cc.Product_id,Numero_Liquidacion=num_liq,Contractor_id=aux_contractor)
                Listo.save()
                valor_nuevo = 0
                Num_Liquidacion.objects.filter(Numero_Liq=num_liq).update(Contractor=aux_contractor)
                ciclo = ciclo+1
            else:
                valor_nuevo = 0
                if aux_contractor == cc.Contractor_id:
                    if cc.Sellado == 'Y':
                        valor_nuevo = valor_nuevo + .01
                    if cc.Barcode == 'Y':
                        valor_nuevo = valor_nuevo + .01

                    valor_nuevo2 = cc.Qty_Delivery * (cc.Product.rate.valor + valor_nuevo)

                    Listo = Liquidacion(Qty_Delivery=cc.Qty_Delivery, valor_unit=cc.Product.rate.valor,
                                        valor_pagado=valor_nuevo2,
                                        fecha_liquidacion=datetime.now(), Orden_id=cc.Orden_id,
                                        Product_id=cc.Product_id, Numero_Liquidacion=num_liq,
                                        Contractor_id=cc.Contractor_id)
                    Listo.save()
                    valor_nuevo = 0
                else:

                    Num_Liquidacion.objects.filter(Numero_Liq=num_liq).update(Contractor=aux_contractor)
                    num_max = Num_Liquidacion.objects.all().order_by('-Numero_Liq')[0]
                    num_max2 = num_max.Numero_Liq + 1
                    nueva_liq = Num_Liquidacion(Numero_Liq=num_max2,Contractor_id=99999)
                    nueva_liq.save()
                    num_liq = num_max2

                    valor_nuevo = 0
                    if cc.Sellado == 'Y':
                        valor_nuevo = valor_nuevo + .01
                    if cc.Barcode == 'Y':
                        valor_nuevo = valor_nuevo + .01

                    valor_nuevo2 = cc.Qty_Delivery * (cc.Product.rate.valor + valor_nuevo)

                    Listo = Liquidacion(Qty_Delivery=cc.Qty_Delivery, valor_unit=cc.Product.rate.valor,
                                        valor_pagado=valor_nuevo2,
                                        fecha_liquidacion=datetime.now(), Orden_id=cc.Orden_id,
                                        Product_id=cc.Product_id, Numero_Liquidacion=num_liq,
                                        Contractor_id=cc.Contractor_id)
                    Listo.save()
                    valor_nuevo = 0
                    Num_Liquidacion.objects.filter(Numero_Liq=num_liq).update(Contractor=cc.Contractor_id)
                    aux_contractor = cc.Contractor_id

        # OrderContractorDetail.objects.filter(id=s).update(Terminado='Y',fecha=datetime.now(),Qty_Delivery=cant_req)
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Orders Contractor'
        context['entidad'] = 'Asesorias'
        context['list_url'] = reverse_lazy('Cobranza:list_order_contractor')
        context['action'] = 'list'
        return context


class Liquidaciones(ListView):
    model = Num_Liquidacion
    template_name = 'Financial/Liquidaciones.html'
    reverse_lazy =  reverse_lazy('Cobranza:reporte_financiero_2')

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detalle_liqui = Num_Liquidacion.objects.all().order_by('-Numero_Liq')
        context['titulo'] = 'Payment Process - Contractors'
        context['Detalle_Orden'] = detalle_liqui
        context['create_url'] = reverse_lazy('Cobranza:generar_pagos2')
        context['list_url'] = reverse_lazy('Cobranza:list_order_contractor')
        context['entidad'] = 'Ready to Pay'
        context['Fase'] = 'Order'
        context['modo'] = 'Editar'
        return context

class print_full_liquidacion(View):

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)

    def get(self, request, *args, **kwargs):
        try:
            valor_x = 0
            template = get_template('Financial/liquidacion_completa.html')
            now = datetime.now() # asi asigno fecha del sistema para que se imprima en el pdf
            orden_master = Liquidacion.objects.filter(Numero_Liquidacion=self.kwargs['Liqui_Num'])
            for aa in orden_master:
                cont_name = aa.Contractor.Name
                valor_x = valor_x + aa.valor_pagado
            num_orden_pcpal = self.kwargs['Liqui_Num']

            context = {
                'Orden_principal': orden_master,
                'num_orden' : str(num_orden_pcpal),
                'nom_contratista': cont_name,
                'valor_total2' : valor_x,
                'comp': {'name': 'SKY LINE USA', 'ruc': 'Phone : 888-800-8440',
                         'address': '4180 St Jhons PkWy , Sanford FL, 32771'},
                'icon': '{}{}'.format(settings.MEDIA_URL, 'LogoGuardog.png'),
                'fecha_a_imprimir' : now
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('Cobranza:list_order_contractor'))

def send_email2(email,asunto,cliente,mora):
    # print(email)
    context = {'mail' : email,'asunto' : asunto,'cliente' : cliente,'mora' : mora}

    template = get_template('correo.html')
    content = template.render(context)
    email = EmailMultiAlternatives(asunto,'',settings.EMAIL_HOST_USER,[email])
    email.attach_alternative(content,'text/html')
    email.send()

@login_required()
def enviar_mail_interno(request):
    # print('Entre a enviar Mail ')
    mensaje_tipo = int(request.POST['msg'])
    datos = []
    if request.method == 'POST':
        send_email2('ferortega1971@hotmail.com','Correo de Prueba','Mateo Fernandez',45)
        linea = 'hola'
        datos.append(linea)
        return JsonResponse({'Result': datos})
    else:
        return HttpResponse("Peticion no valida")



@login_required()
def reporte_nuevo_asembly_log(request): #Reporte para imprimir todos los dias el cuadre de caja
    data = []

    if request.method == 'POST':
        fecha_ini = request.POST['fecha1']
        fecha_fin = request.POST['fecha2']
        if fecha_fin == '':
            fecha_fin=fecha_ini
        if fecha_ini > fecha_fin:
            print("error en fechas")
            mensaje = "Fecha Inicial NO puedo ser mayor que fecha final"
            data = {'mensaje' : mensaje,
                    'titulo': 'Assembly Log by Dates'}
            return render(request, 'Contractors/list_asembly_log.html', data)

        if fecha_ini == '':
            fecha_ini = datetime.now().strftime("%Y-%m-%d")
            fecha_fin = datetime.now().strftime("%Y-%m-%d")
            data = {
                'titulo': 'Assembly Log - '+ fecha_ini + ' a '+ fecha_fin, 'fecha1':fecha_ini,'fecha2':fecha_fin,
                'url': '/App/OrderContractor/report_log/'+fecha_ini+'/'+fecha_fin+'/' ,
                'url3': '/App/OrderContractor/report_log/' + fecha_ini + '/' + fecha_fin + '/',
                'pagos': OrderContractorDetail.objects.filter(fecha__gte=fecha_ini,fecha__lte=fecha_fin)
            }
            return render(request, 'Contractors/list_asembly_log.html', data)
        else:
            if fecha_fin == '':
                fecha_fin = fecha_ini
                fecha_fin = datetime.now().strftime("%Y-%m-%d")
                data = {
                    'titulo': 'Assembly Log - '+ fecha_ini + ' a '+ fecha_fin, 'fecha1': fecha_ini,
                    'fecha2': fecha_fin,
                    'url': '/App/OrderContractor/report_log/'+fecha_ini+'/'+fecha_fin+'/' ,
                    'url3': '/App/OrderContractor/report_log/' + fecha_ini + '/' + fecha_fin + '/',
                    'pagos': OrderContractorDetail.objects.filter(fecha__gte=fecha_ini,fecha__lte=fecha_fin)
                }
                return render(request, 'Contractors/list_asembly_log.html', data)
            else:
                data = {
                    'titulo': 'Assembly Log -  From : ' + fecha_ini + ' to ' + fecha_fin ,
                    'url': '/App/OrderContractor/report_log/'+fecha_ini+'/'+fecha_fin+'/' ,
                    'url3': '/App/OrderContractor/report_log/' + fecha_ini + '/' + fecha_fin + '/',
                    'pagos': OrderContractorDetail.objects.filter(fecha__gte=fecha_ini,fecha__lte=fecha_fin)}
                return render(request, 'Contractors/list_asembly_log.html', data)

    else:
        fecha_ini = datetime.now().strftime("%Y-%m-%d")
        fecha_fin = '2030-12-31'
        data = {
           # 'Fecha_Cierre' : Fecha_Cierre.objects.all(),
            'titulo': 'Assembly Log -  From : ' + fecha_ini + ' to ' + fecha_fin ,
            'fecha1': fecha_ini,
            'fecha2': fecha_fin,
            'url': '/App/OrderContractor/report_log/' + fecha_ini + '/' + fecha_fin + '/',
            'url3': '/Cobranza/Caja/cierre_diario3/' + fecha_ini + '/' + fecha_fin + '/',
            'url4': '/Cobranza/Caja/cierre_caja_real/',
            'url5': '/Cobranza/Caja/traslado_a_boveda/',
            'url6': '/Cobranza/Caja/consignacion/',
            'es_Cajero' : 99,
            'pagos': OrderContractorDetail.objects.filter(fecha__gte=fecha_ini,fecha__lte=fecha_fin)}
        return render(request, 'Contractors/list_asembly_log.html',data)

class producto_en_quickbooks(ListView): #
    model = OrderContractorDetail
    template_name = 'Contractors/list2.html'  # Plantilla que usara
    success_url = reverse_lazy('Contractors/list2.html')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            s = 0
            # Con esto accedo a los parametros de Kwargs
            for key, value in self.kwargs.items():
                # print(key, "=", value)
                s = value
                # context['plan'] = value
            # Aqui enviado el listado de unicamente lo que quiero mostrar
            cant = OrderContractorDetail.objects.filter(id=s)
            for cantid in cant:
                cant_req = cantid.Qty_Req
            OrderContractorDetail.objects.filter(id=s).update(En_QuickB='Y', fecha_quickbook=datetime.now())
            # send_email2('ferortega1971@hotmail.com','Prueba2','Fer Ortega',1)
            for a in cant:
                orden_afectada = a.Orden_id

            request.path = ''
            request.path_info = ''
            return redirect('/App/OrderContractor/listDeliverPlus/'+str(orden_afectada))

        return super().dispatch(request, *args, **kwargs)

    # def get_queryset(self):
    #     lista = OrderContractor.objects.filter(closed='N')
    #     return lista

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Orders Contractor'
        context['entidad'] = 'Asesorias'
        context['list_url'] = reverse_lazy('Cobranza:list_order_contractor_entregado')
        context['action'] = 'list'
        return context

login_required()
class Reporte_Assembly_Log(View): # Impresion de Recibo

    es_Cajero = 999
    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            # template = get_template('Caja/cierre_diario.html')
            template = get_template('Contractors/Assembly_Log_Pdf.html')
            now = datetime.now() # asi asigno fecha del sistema para que se imprima en el pdf
            fecini=self.kwargs['fec1']
            fecfin=self.kwargs['fec2']
            orden_detaile = OrderContractorDetail.objects.filter(Terminado='Y',fecha__gt=fecini,fecha__lt=fecfin).order_by('fecha')
            #
            context = {
                'comp': {'name': 'SKY LINE USA', 'ruc': 'Phone : 888-800-8440',
                         'address': '4180 St Jhons PkWy , Sanford FL, 32771'},
                'icon': '{}{}'.format(settings.MEDIA_URL, 'LogoGuardog.png'),
                'fecha_a_imprimir' : now,
                'usuario_logeado' : request.user.username,
                'Orden_detalle3':orden_detaile,
                'fecha_inicial':fecini,
                'fecha_final':fecfin,

            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('Cobranza:reporte_caja_list'))