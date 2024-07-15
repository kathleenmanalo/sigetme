from django.urls import path

# from Modulos.Cobranza.Vistas.CentroControl.views import *
# from Modulos.Cobranza.Vistas.Ciudades.views import *
# from Modulos.Cobranza.Vistas.Clientes.views import *
# from Modulos.Cobranza.Vistas.Cartera.views import *
# from Modulos.Cobranza.Vistas.Asesorias.views import *
# from Modulos.Cobranza.Vistas.Gastos.views import *
# from Modulos.Cobranza.Vistas.CarteraTotales.views import *
# from Modulos.Cobranza.Vistas.Observaciones.views import *
# from Modulos.Cobranza.Vistas.Dashboard.views import *
# from Modulos.Cobranza.Vistas.Prestamos.views import *
# from Modulos.Cobranza.Vistas.Prestamistas.views import *
from Modulos.guardog_wh.Vistas.Customers.views import CustomersListView

from Modulos.guardog_wh.Vistas.Order.views import *
from Modulos.guardog_wh.Vistas.Contractors.views import *
from Modulos.guardog_wh.Vistas.ControlCenter.views import *

app_name = 'Cobranza'


urlpatterns = [
    # path('Ciudades/list/', CiudadesListView.as_view(), name='ciudades_list'),
    # path('Ciudades/list2/', ciudades_list, name='ciudades_list2'),
    # path('Ciudades/crear/', CiudadesCreateView.as_view(), name='ciudades_crear'),
    # #
    # path('Clientes/list/', ClientesListView.as_view(), name='clientes_list'),
    # path('Clientes/list2/', clientes_list, name='clientes_list2'),
    # path('Clientes/crear/', ClientesCreateView.as_view(), name='clientes_crear'),
    # path('Clientes/update/<int:pk>/', ClientesUpdateView.as_view(), name='clientes_update'),

    # #
    # path('Cartera/list/', CarteraListView.as_view(), name='cartera_list'),
    # path('Cartera/list_rp/', CarteraList_RP_View.as_view(), name='cartera_list_rec_pago'),
    # path('Cartera/list_rp_mail/', CarteraList_RP_Mail_View.as_view(), name='cartera_list_rec_pago_mail'),
    # path('Cartera/RepCobranza/', RepCarteraListView.as_view(), name='reporte_cartera_xls'),

    # path('Asesorias/list/', AsesoriasListView.as_view(), name='asesorias_list'),
    # path('Asesorias/list_analisis/', AsesoriasListViewAnalisis.as_view(), name='asesorias_list_analisis'),
    # path('Asesorias/list_verifica/', AsesoriasListViewVerifica.as_view(), name='asesorias_list_verifica'),
    # path('Asesorias/list_aprobacion/', AsesoriasListViewAprobacion.as_view(), name='asesorias_list_aprobacion'),
    # path('Asesorias/list_desembolso/', AsesoriasListViewDesembolso.as_view(), name='asesorias_list_desembolso'),
    # path('Asesorias/list_historia/', AsesoriasListViewHistoria.as_view(), name='asesorias_list_historia'),
    # path('Asesorias/list2/', asesorias_list, name='asesorias_list2'),
    # path('Asesorias/crear/', AsesoriasCreateView.as_view(), name='asesorias_crear'),
    # path('Asesorias/update/<int:pk>/', AsesoriasUpdateView.as_view(), name='asesorias_update'),
    # path('Asesorias/update_analisis/<int:pk>/', AsesoriasUpdateViewAnalisis.as_view(), name='asesorias_update_analisis'),
    # path('Asesorias/update_verificacion/<int:pk>/', AsesoriasUpdateViewVerificacion.as_view(), name='asesorias_update_verificacion'),
    # path('Asesorias/update_codeudor/<int:pk>/', AsesoriasUpdateViewCodeudor.as_view(), name='asesorias_update_codeudor'),
    # path('Asesorias/update_retanqueo/<int:pk>/', AsesoriasUpdateViewRetanqueo.as_view(), name='asesorias_update_retanqueo'),
    # path('Asesorias/update_aprobacion/<int:pk>/', AsesoriasUpdateViewAprobacion.as_view(), name='asesorias_update_aprobacion'),
    # path('Asesorias/update_desembolso/<int:pk>/', AsesoriasUpdateViewDesembolso.as_view(), name='asesorias_update_desembolso'),
    # path('Asesorias/delete/<int:pk>/', AsesoriasDeleteView.as_view(), name='asesorias_delete'),
    # path('Asesorias/plan/<int:pk>/', vista_plan.as_view(), name='asesorias_ver_plan'),
    # path('Asesorias/plan/', vista_sumar, name='asesorias_plan'),
    # path('Asesorias/retomar/<int:pk>/', vista_plan.as_view(), name='asesorias_retomar'),

    # # Mensajeria
    # path('Asesorias/enviar_msg1/', enviar_msg, name='enviar_msg1'),
    # #
    # path('Asesorias/siguientefase/<int:pk>/', sgte_fase.as_view(), name='siguiente_fase'),
    # path('Asesorias/rechazar_asesoria/<int:pk>/', rechazar_asesoria.as_view(), name='rechazar_asesoria'),

    # path('PrestamosVip/list/', ConsignacionesListView.as_view(), name='consignaciones_list'),
    # path('PrestamosVip/crear/', ConsignacionesCreateView.as_view(), name='consignaciones_crear'),


    # path('Gastos/list/', GastosListView.as_view(), name='gastos_list'),
    # path('Gastos/ingresos/', IngresosListView.as_view(), name='ingresos_list'),
    # path('Gastos/list2/', gastos_list, name='gastos_list2'),
    # path('Gastos/crear/', GastosCreateView.as_view(), name='gastos_crear'),
    # path('Gastos/crear_ing/', IngresosCreateView.as_view(), name='ingresos_crear'),
    # path('Gastos/update/<int:pk>/', GastosUpdateView.as_view(), name='gastos_update'),
    # path('Gastos/delete/<int:pk>/', GastosDeleteView.as_view(), name='gastos_delete'),

    # path('CarteraTotales/list/', CarteraTotalesListView.as_view(), name='carteratotales_list'),
    # path('CarteraTotales/list2/', gastos_list, name='carteratotales_list2'),
    # path('CarteraTotales/crear/', CarteraTotalesCreateView.as_view(), name='carteratotales_crear'),
    # path('CarteraTotales/update/<int:pk>/', CarteraTotalesUpdateView.as_view(), name='carteratotales_update'),
    # path('CarteraTotales/delete/<int:pk>/', CarteraTotalesDeleteView.as_view(), name='carteratotales_delete'),

    # path('Prestamos/list_filter/', prestamos_list, name='prestamos_list_filter'),
    # path('Prestamos/plan_cuotas/<int:pagare>/', prestamos_plan_cuotas, name='prestamos_plan_cuotas'),
    # # Plan de Pagos Original
    # path('Prestamos/plan_cuotas_pdf/<int:pagare>/', PrestamoPdfView.as_view(),name='prestamo_plan_pdf'),
    # path('Prestamos/desembolso/<int:pagare>/', PrestamoPdfView_desembolso.as_view(),name='prestamo_desembolso_pdf'),
    # #Impresion de Recibo de Pago en PDF
    # path('Prestamos/recibo_pdf/<int:recibo>/', PrestamoReciboPdfView.as_view(),name='prestamo_recibo_pdf'),
    # path('Prestamos/pagos_pagare_pdf/<int:pagare>/', Prestamo_Pagos_PdfView.as_view(),name='prestamo_pagos_pdf'),
    # # Estado de cuenta
    # path('Prestamos/plan_estado_pdf/<int:pagare>/', PrestamoPdfEstadoView.as_view(),name='prestamo_estado_pdf'),
    # path('Prestamos/pagos/<int:pagare>/', PagarPrestamo.as_view(),name='prestamo_pagos'),
    # path('Prestamos/pago_total/<int:pagare>/', PagarPrestamoTotal.as_view(),name='prestamo_pago_total'),
    # path('Prestamos/pago_total_retanqueo/<int:pagare>/', PagarPrestamoTotalRetanqueo.as_view(),name='prestamo_pago_retanqueo'),
    # path('Prestamos/condonar_mora/<int:pagare>/', CondonarMora.as_view(),name='condonar_mora'),
    # path('Prestamos/condonar_interes/<int:pagare>/', CondonarInteres.as_view(),name='condonar_interes'),
    # path('Prestamos/pagos_capital/<int:pagare>/', PagarPrestamoCapital.as_view(),name='prestamo_pagos_capital'),
    # path('Prestamos/pagos_capital2/<int:pagare>/', PagarPrestamoCapital2.as_view(),name='prestamo_pagos_capital2'),
    # path('Prestamos/hist_pagos/<int:pagare>/', HistoPagos.as_view(),name='prestamo_hist_pagos'),
    # path('Prestamos/list_filter/', prestamos_list, name='prestamos_list_filter'),
    # path('Prestamos/list_filter_2/', prestamos_list_2, name='prestamos_list_filter_2'),
    # path('Prestamos/reporte_caja/', reporte_caja_list,name='reporte_caja_list'),
    # path('Prestamos/libro_diario/', libro_diario_1,name='libro_diario_1'),
    # path('Prestamos/reporte_colocaciones/', reporte_colocaciones,name='reporte_colocaciones'),

    # path('Prestamos/pagos2/', aplicar_pago, name='aplicar_pago'),
    # path('Prestamos/pago_total/', aplicar_pago_total, name='aplicar_pago_total'),
    # path('Prestamos/pago_total_r/', aplicar_pago_total_r, name='aplicar_pago_total_r'),
    # path('Prestamos/pago_mora/', aplicar_pago_mora, name='aplicar_pago_mora'),
    # path('Prestamos/pago_interes/', aplicar_pago_interes, name='aplicar_pago_interes'),
    # # Aplicar pago a capital - cuota igual
    # path('Prestamos/pagos3/', aplicar_pago_cap, name='aplicar_pago_cap'),
    #  # Aplicar pago a capital - con reduccion de cuota - mismo plazo
    # path('Prestamos/pagos4/', aplicar_pago_cap2, name='aplicar_pago_cap2'),

    # path('Prestamos/enviar_mail/', enviar_mail, name='enviar_mail'),


    # path('Observaciones/list_filter/', observaciones_list, name='observaciones_list_filter'),
    # path('Observaciones/list/', ObservacionesListView.as_view(), name='observaciones_list'),
    # path('Observaciones/list3/', ObservacionesListView3.as_view(), name='observaciones_list3'),
    # path('Observaciones/list4/', ObservacionesListView2.as_view(), name='observaciones_list4'),
    # path('Observaciones/realizadas_hoy/', ObservacionesHoy.as_view(), name='observaciones_hoy'),
    # path('Observaciones/tareas_para_hoy/', TareasParaHoy.as_view(), name='tareas_para_hoy'),
    # path('Observaciones/para_realizar/', ObservacionesManana.as_view(), name='observaciones_manana'),
    # path('Observaciones/list2/', observaciones_list, name='observaciones_list2'),
    # path('Observaciones/crear/', ObservacionesCreateView.as_view(), name='observaciones_crear'),
    # path('Observaciones/update/<int:pk>/', ObservacionesUpdateView.as_view(), name='observaciones_update'),
    # path('Observaciones/delete/<int:pk>/', ObservacionesDeleteView.as_view(), name='observaciones_delete'),

    # path('Dashboard/', DashboardView2.as_view(), name='Dashboard'),

    # path('Caja/cierre_diario2/<str:fec1>/<str:fec2>/', CierreCajaPdfView.as_view(),name='cierre_diario_pdf2'),
    # path('Caja/cierre_diario3/<str:fec1>/<str:fec2>/', CierreCajaDetPdfView.as_view(),name='cierre_diario_pdf3'),
    # #
    # path('Caja/cierre_caja_real/', cierre_caja_real_1,name='cierre_caja_r'),
    # path('Caja/traslado_a_boveda/', traslado_a_boveda_1,name='traslado_a_boveda'),
    # path('Caja/consignacion/', consignacion_1,name='consignacion'),
    # path('Caja/libro_diario2/<str:fec1>/<str:fec2>/', libro_diario_2.as_view(),name='libro_diario_pdf2'),
    # #
    # path('Prestamos/detallado_colocacion/<str:fec1>/<str:fec2>/', detallado_colocacion_pdf.as_view(),name='detallado_colocacion'),
    # # path('Prestamos/recibo_pdf/<int:recibo>/', PrestamoReciboPdfView.as_view(),name='prestamo_recibo_pdf'),

    # path('Prestamos/detalle_cartera/', detalle_cartera,name='detalle_cartera'),

    # path('Turnos/list/', TurnosListView.as_view(), name='turnos_list'),
    # path('Turnos/tareas_para_hoy/', TurnosParaHoy.as_view(), name='turnos_hoy'),

    path('Orders/crear/', OrderCreateView.as_view(), name='order_create'),
    path('Orders/list/<int:id>/', OrderListView.as_view(), name='order_list'),
    path('Orders/update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('Orders/list2/', order_list2, name='order_list2'),
    path('Orders/AddItems/<int:order>/', AddItemToOrder.as_view(),name='add_item_to_order'),
    path('Orders/additem2/', add_item2, name='add_item2'),
    path('Orders/Dunhams/LabelInnerBox/<int:orden_id>/', LabelSmallBoxDunhams.as_view(),name='label_inner_Dunhams'),
    path('Orders/Menards/LabelInnerBox2/<int:orden_id>/', LabelSmallBoxMenards.as_view(),name='label_inner_Menards'),
    path('Orders/Menards/LabelInnerBox3/<int:orden_id>/', LabelSmallBoxAcademy.as_view(),name='label_inner_Academy'),


    path('Customers/list/', CustomersListView.as_view(), name='customers_list'),

    # Urls para control de contratistas
    path('OrderContractor/crear/', Ord_Contrac_CreateView.as_view(), name='create_order_contractor'),
    path('OrderContractor/list/', Ord_Contrac_ListView.as_view(), name='list_order_contractor'),
    path('OrderContractor/listOpen/', Ord_Contrac_ListView_Open.as_view(), name='list_order_contractor_open'),
    path('OrderContractor/listClose/', Ord_Contrac_ListView_Close.as_view(), name='list_order_contractor_close'),
    path('OrderContractor/listDeliver/', Ord_Contrac_ListView_Entregado.as_view(), name='list_order_contractor_entregado'),
    path('OrderContractor/listDeliverPlus/<int:id>', Ord_Contrac_ListView_EntrePlus.as_view(), name='list_order_contractor_entregado_plus'),
    path('OrderContractor/listDeliver2/', reporte_nuevo_asembly_log,name='reporte_entregado2'),
    path('OrderContractor/list_det/<int:id>', Ord_Contrac_ListView_det.as_view(), name='list_order_detail_contractor'),
    path('OrderContractor/update_det/<int:pk>/', OrderUpdateDetailView.as_view(), name='order_update_detail'),
    path('OrderContractor/delete_det/<int:pk>/', OrderDeleteDetailView.as_view(), name='order_delete_detail'),
    path('OrderContractor/AddItems/<int:id>/', AddItemToOrder_Cont.as_view(),name='add_item_to_order_contractor'),
    # path('OrderContractor/AddItems/', AddItemToOrder_Cont.as_view(),name='add_item_to_order_contractor'),
    path('OrderContractor/Print_full_order/<int:order>/', print_full_order_cont.as_view(),name='print_full_ordercontractor'),
    path('OrderContractor/Aprobar/<int:pk>/', Aprobar_Orden.as_view(), name='aprobar_orden'),

    path('ControlCenter/', DashboardView2.as_view(), name='Dashboard2'),


    path('OrderContractor/AddItemsVer2/<int:id>/', AddItemToOrder_Cont_V2.as_view(),name='add_item_order_contrac_v2'),
    path('OrderContractor/Termiando/<int:pk>/', producto_terminado.as_view(), name='producto_terminado'),
    path('OrderContractor/EnQuickbook/<int:pk>/', producto_en_quickbooks.as_view(), name='producto_en_quickbook'),
    path('OrderContractor/additem3/', add_item3, name='add_item2'),

    path('Financial/initial_report/', Reporte_Inicial_Financiero.as_view(), name='reporte_financiero_1'),
    path('Financial/liquidaciones/', Liquidaciones.as_view(), name='reporte_financiero_2'),
    path('Financial/Print_full_liq/<int:Liqui_Num>/', print_full_liquidacion.as_view(),name='print_full_liquidacion'),

    path('Financial/generate_file/', Generar_Pagos2.as_view(), name='generar_pagos2'),

    path('OrderContractor/enviar_mail_interno/', enviar_mail_interno, name='enviar_mail_int'),
    path('OrderContractor/report_log/<str:fec1>/<str:fec2>/', Reporte_Assembly_Log.as_view(),name='rep_as_log2'),
]

