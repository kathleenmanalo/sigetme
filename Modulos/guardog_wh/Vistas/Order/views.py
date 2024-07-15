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

from django.conf import settings
from sigetme.settings import *


class OrderCreateView(ValidatePermissionRequiredMixin, CreateView):
    permission_required = 'Cobranza.add_order'
    url_redirect = reverse_lazy('Cobranza:customers_list')
    model = Order
    form_class = OrderForm
    template_name = 'Orders/create.html'  # Plantilla que usara mi CreateView o creador de formularios
    success_url = reverse_lazy('Cobranza:customers_list')



    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        order_id = self.kwargs.get('order')
        orden = Order.objects.filter(id=order_id).first()
        
        if orden:
            cust_identif = orden.customer_id
            cust = orden.customer.name
            so_number = orden.So_number
            order_id2 = orden.id
        else:
            cust_identif = ''
            cust = ''
            so_number = ''
            order_id2 = 0
        
        orden_detalle = OrderDetails.objects.filter(Orden_id=order_id)
        sum_small_box = sum(ot.QtySmallBox for ot in orden_detalle)
        sum_tot_items = sum(ot.Ordered_Qty for ot in orden_detalle)

        WeightSheet4 = WeightSheet.objects.filter(Orderx_id=order_id2)
        totalpeso = sum(totp.Weight for totp in WeightSheet4)

        now = datetime.now()

        context.update({
            'titulo': 'Adding items to S.O No.',
            'entidad': 'Order Details',
            'num_order': so_number,
            'cust_id': cust_identif,
            'tot_cajas_peque': sum_small_box,
            'total_items': sum_tot_items,
            'orden_id': order_id,
            'cust': cust,
            'list_url': reverse_lazy('Cobranza:customers_list'),
            'action': 'nueva',
            'order_detalle': orden_detalle,
            'Ws5': WeightSheet4,
            'total_peso_con_palet': totalpeso + 45,
            'fecha_a_imprimir': now,
            'Orden_id2': order_id2
        })

        return context


class OrderListView(ListView):
    model = Order
    template_name = 'Orders/list.html'
    reverse_lazy = 'Orders/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
         lista = Order.objects.filter(customer_id=self.kwargs['id'])
         return lista

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Order.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # Basicamente todas estas son variables que despues las puedo usar en mi html respectivo
    # es muy util usar esto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Order Report'
        context['create_url'] = reverse_lazy('Cobranza:order_create')
        context['list_url'] = reverse_lazy('Cobranza:customers_list')
        context['entidad'] = 'Orders'
        context['Fase'] = 'Order'
        context['modo'] = 'Editar'
        return context

class OrderUpdateView(ValidatePermissionRequiredMixin,UpdateView): # Esto es para crear un formulario de Asesorias
    permission_required = 'Cobranza.change_asesorias'
    url_redirect = reverse_lazy('Cobranza:customers_list')
    model = Order
    form_class = OrderForm
    template_name = 'Orders/update.html'  # Plantilla que usara mi CreateView o creador de formularios
    success_url = reverse_lazy('Cobranza:customers_list')

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

        context['titulo'] = 'Edit Order'
        context['entidad'] = 'Asesorias'
        context['list_url'] = reverse_lazy('Cobranza:customers_list')
        context['action'] = 'edit'
        return context

@login_required()
def order_list2(request):

    es_Cajero = 0
    for g in request.user.groups.all():
        # print(g.name)
        if g.name == 'Cajero' or g.name == 'Administrador':
            es_Cajero = 1

    data = {
        'titulo': 'Order Report ',
        'Cartera': Order.objects.all().order_by('-id'),

    }
    return render(request, 'Orders/list2.html', data)

class AddItemToOrder(ValidatePermissionRequiredMixin,CreateView): # Esto es para crear un formulario de Asesorias
    permission_required = 'Cobranza.add_pagos3'
    url_redirect = reverse_lazy('Cobranza:customers_list')
    model = OrderDetails
    form_class = OrderDetailsForm
    template_name = 'Orders/additemtoorder.html'  # Plantilla que usara mi CreateView o creador de formularios
    success_url = reverse_lazy('Cobranza:customers_list')



    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):

        a = self.kwargs['order']
        kwargs['dato1']=11
        intial_data = {
            'name': 'Student1',
            'roll': 123456,
            'orden2': a
        }

        # form = OrderDetailsForm(initial=intaial_data)


        context = super().get_context_data(**kwargs)

        kwargs['dato2'] = 2211
        

        orden = Order.objects.filter(id=self.kwargs['order'])
        order_id2 = 0
        so_number = 0
        cust_identif = 0
        cust = 0
        

        for la in orden:
            cust_identif = la.customer_id
            cust = la.customer.name
            so_number = la.So_number
            order_id2 = la.id
        orden_detalle = OrderDetails.objects.filter(Orden_id=self.kwargs['order'])
        sum_small_box = 0
        sum_tot_items = 0
        for ot in orden_detalle:
            sum_small_box = sum_small_box + ot.QtySmallBox
            sum_tot_items = sum_tot_items + ot.Ordered_Qty

        WeightSheet4 = WeightSheet.objects.filter(Orderx_id=order_id2)
        totalpeso = 0
        for totp in WeightSheet4:
            totalpeso = totalpeso+totp.Weight

        now = datetime.now()  # asi asigno fecha del sistema para que se imprima en el pdf

        context['titulo'] = 'Adding items to S.O No. '
        context['entidad'] = 'Order Details'
        context['num_order'] = so_number
        context['cust_id'] = cust_identif
        context['tot_cajas_peque'] = sum_small_box
        context['total_items'] = sum_tot_items
        context['orden_id'] = self.kwargs['order']
        context['cust'] = cust
        context['list_url'] = reverse_lazy('Cobranza:customers_list')
        context['action'] = 'nueva'

        context['order_detalle'] = orden_detalle
        context['Ws5'] = WeightSheet4
        context['total_peso_con_palet'] = totalpeso + 45
        context['fecha_a_imprimir'] = now
        context['Orden_id2'] = order_id2

        return context


@login_required()
def add_item2(request):
    print('Adding ITEM.....')
    datos = []
    if request.method == 'POST':
        cust_idx = int(request.POST['cust_id4'])
        prod_idx = int(request.POST['prod2'])
        order_idx = int(request.POST['orden2'])
        qty_x = int(request.POST['qty2'])
        small_box= 0
        big_box = 0

        Orden_Principal = Order.objects.filter(id=order_idx)
        for OP in Orden_Principal:
            po_number = OP.Po_number
            destino = OP.shipto.ShipTo

        matrix_req = Matrix.objects.filter(Customer_id=cust_idx,Prod_id=prod_idx)
        for iii in matrix_req:
             BoxType_Id2 = iii.BoxType_id
             Nombre_Prod = iii.Prod.code
             inner_label = iii.ImgLabelSmallBox
             box_label = iii.ImgLabelMasterBox
             Sku_prod = iii.SKU
        InfoType = BoxType2.objects.filter(BoxType = BoxType_Id2)
        for jjj in InfoType:
            QtyinSmallBox_x = jjj.QtySmallBox
            QtyinMasterBox_x = jjj.QtySmallBox_inMaster
            Tot_en_cada_caja = jjj.QtySmallBox * jjj.QtySmallBox_inMaster
            weigh_x = jjj.WeighMasterBox
            net_weigh = jjj.NetWeighMasterBox
            dim_x = jjj.SizeMasterBox
        small_box = int(qty_x/ QtyinSmallBox_x)

        OrdDet = OrderDetails(Orden_id = order_idx,Prod_id=prod_idx,Ordered_Qty=qty_x,QtySmallBox=small_box,QtyBigBox=big_box)
        OrdDet.save()
        iteraciones = int(small_box)
        for i in range(1, iteraciones+1, 1):
            SmallLabel = OrderDetailsInner(Orden_id=order_idx, Cantidad=qty_x / small_box, ProductName=Nombre_Prod,Archivo_imagen=inner_label)
            SmallLabel.save()


        ProductWS = Product.objects.filter(id=prod_idx)
        for prows in ProductWS:
            prod_name = prows.name
            color_prod = prows.color

        cuantas_llevo = 0
        WeightSheet3 = WeightSheet.objects.filter(Orderx_id=order_idx)
        for cuantas_box in WeightSheet3:
            cuantas_llevo = cuantas_llevo + 1

        cuantas_llevo = cuantas_llevo + 1
        ciclos = small_box / QtyinMasterBox_x
        numero = 0
        while numero < ciclos:
            numero = numero + 1
            WeightSheet2 = WeightSheet(Orderx_id=order_idx,BoxNumber=cuantas_llevo,ProductName=prod_name,Weight=weigh_x,Dimensions=dim_x,Barcode_image=box_label,SKU_p=Sku_prod,Weight_Net=net_weigh,Total_of_Items=Tot_en_cada_caja,
                                       PO_Num=po_number,Destino_final=destino,color=color_prod)
            WeightSheet2.save()
            cuantas_llevo = cuantas_llevo + 1


        print('Aqui acabe de grabar')
        datos.append(100)
        return JsonResponse({'Result': datos})
    else:
        return HttpResponse("Peticion no valida")


class LabelSmallBoxDunhams(View): # Impresion de Recibo

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
            template = get_template('Orders/Dunhams/inner_box.html')
            now = datetime.now() # asi asigno fecha del sistema para que se imprima en el pdf
            detalla_orden = OrderDetailsInner.objects.filter(Orden_id=self.kwargs['orden_id'])
            arreglo1 = OrderDetailsInner.objects.filter(Orden_id=self.kwargs['orden_id'])[:7]
            arreglo2 = OrderDetailsInner.objects.filter(Orden_id=self.kwargs['orden_id'])[:1]
            tot_cajas = 0
            for do in detalla_orden:
                tot_cajas = tot_cajas + 1


            context = {
                'Detalle':detalla_orden,
                'contador_gral':tot_cajas,
                'contador':1,
                'arreglo2': arreglo2,
                'arreglo1':arreglo1,
                # 'asesor_html': asesor,
                'comp': {'name': 'CREDISOÑAR SAS', 'ruc': '901.122.690-4', 'address': 'Calle 22 Num 5-71 Pasto - Nariño'},
                'icon2': '{}{}'.format(settings.MEDIA_URL, 'LogoGuardog22.png'),
                'fecha_a_imprimir' : now,
                'usuario_logeado' : request.user.username
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
        return HttpResponseRedirect(reverse_lazy('Cobranza:prestamos_list_filter'))


class LabelSmallBoxMenards(View): # Impresion de Recibo

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
            template = get_template('Orders/Menards/inner_master.html')
            now = datetime.now() # asi asigno fecha del sistema para que se imprima en el pdf
            orden_pcpal = Order.objects.filter(id=self.kwargs['orden_id'])
            detalla_orden = OrderDetailsInner.objects.filter(Orden_id=self.kwargs['orden_id'])
            master = WeightSheet.objects.filter(Orderx_id=self.kwargs['orden_id'])
            total_de_cajas = 0
            for xx in master:
                total_de_cajas = total_de_cajas + 1
            arreglo1 = OrderDetailsInner.objects.filter(Orden_id=self.kwargs['orden_id'])[:7]
            tot_cajas = 0
            for do in detalla_orden:
                tot_cajas = tot_cajas + 1


            context = {
                'Detalle':detalla_orden,
                'Master': master,
                'Orden_1': orden_pcpal,
                'contador_gral':tot_cajas,
                'tot_cajas_total' : total_de_cajas,
                'contador':1,
                'arreglo1':arreglo1,
                # 'asesor_html': asesor,
                'comp': {'name': 'CREDISOÑAR SAS', 'ruc': '901.122.690-4', 'address': 'Calle 22 Num 5-71 Pasto - Nariño'},
                'icon2': '{}{}'.format(settings.MEDIA_URL, 'HornetInner.png'),
                'fecha_a_imprimir' : now,
                'usuario_logeado' : request.user.username
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
        return HttpResponseRedirect(reverse_lazy('Cobranza:prestamos_list_filter'))


class LabelSmallBoxAcademy(View): # Impresion de Recibo

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
            template = get_template('Orders/Academy/box_labels.html')
            now = datetime.now() # asi asigno fecha del sistema para que se imprima en el pdf
            orden_pcpal = Order.objects.filter(id=self.kwargs['orden_id'])
            detalla_orden = OrderDetailsInner.objects.filter(Orden_id=self.kwargs['orden_id'])
            master = WeightSheet.objects.filter(Orderx_id=self.kwargs['orden_id'])
            total_de_cajas = 0
            for xx in master:
                total_de_cajas = total_de_cajas + 1
            arreglo1 = OrderDetailsInner.objects.filter(Orden_id=self.kwargs['orden_id'])[:7]
            tot_cajas = 0
            for do in detalla_orden:
                tot_cajas = tot_cajas + 1


            context = {
                'Detalle':detalla_orden,
                'Master': master,
                'Orden_1': orden_pcpal,
                'contador_gral':tot_cajas,
                'tot_cajas_total' : total_de_cajas,
                'contador':1,
                'arreglo1':arreglo1,
                # 'asesor_html': asesor,
                'comp': {'name': 'CREDISOÑAR SAS', 'ruc': '901.122.690-4', 'address': 'Calle 22 Num 5-71 Pasto - Nariño'},
                'icon2': '{}{}'.format(settings.MEDIA_URL, 'HornetInner.png'),
                'fecha_a_imprimir' : now,
                'usuario_logeado' : request.user.username
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
        return HttpResponseRedirect(reverse_lazy('Cobranza:prestamos_list_filter'))




