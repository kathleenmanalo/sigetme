from django.db import models
from datetime import datetime


class PSpray_Types(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', default='')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.name)

    class Meta:
        verbose_name = 'P.Spray Type'
        verbose_name_plural = 'P.Spray Type'


class Estados(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', default='')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.name)

    class Meta:
        verbose_name = 'Estate'
        verbose_name_plural = 'Estates'


class Cities(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', default='')
    estado = models.ForeignKey(Estados, on_delete=models.PROTECT, null=False, blank=False, default='')

    def __str__(self):
        txt = "{0}"
        return txt.format(self.name)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', default='')
    address = models.CharField(max_length=100, verbose_name='Address', default='')

    def __str__(self):
        txt = " {0} "
        return txt.format(self.name)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class rates(models.Model):
    code = models.CharField(max_length=30, verbose_name='Code', default='')
    name = models.CharField(max_length=100, verbose_name='Name', default='')
    valor = models.FloatField(default=1)

    def __str__(self):
        txt = "{0} "
        return txt.format(self.name)

    class Meta:
        verbose_name = 'Rates'
        verbose_name_plural = 'Rates'


class Product(models.Model):
    code = models.CharField(max_length=30, verbose_name='Code', default='')
    name = models.CharField(max_length=100, verbose_name='Name', default='')
    color = models.CharField(max_length=100, verbose_name='Color', default='')
    nombre = models.CharField(max_length=100, verbose_name='Name2', default='')
    tipo_p_spray = models.ForeignKey(PSpray_Types, on_delete=models.PROTECT, null=True, blank=True)
    # image = models.ImageField(upload_to='')
    barcode = models.CharField(max_length=30, verbose_name='Barcode', default='123456789')
    rate = models.ForeignKey(rates, on_delete=models.PROTECT, null=True, blank=True)
    si_no = [('Y', 'Yes'), ('N', 'Not')]
    only_labeling = models.CharField(max_length=1, choices=si_no, default='N')
    active = models.CharField(max_length=1, choices=si_no, default='Y')
    menards = models.CharField(max_length=1, choices=si_no, default='N')
    dunams = models.CharField(max_length=1, choices=si_no, default='N')
    academy = models.CharField(max_length=1, choices=si_no, default='N')
    contractor = models.CharField(max_length=1, choices=si_no, default='N')

    def __str__(self):
        txt = "{0}"
        return txt.format(self.name)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']


class Destinos(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False, blank=False, default='')
    ShipTo = models.CharField(max_length=100, verbose_name='ShipTo', default='')
    citi = models.ForeignKey(Cities, on_delete=models.PROTECT, null=False, blank=False, default='')
    zipcode = models.CharField(max_length=10, verbose_name='ZipCode', default='')

    def __str__(self):
        txt = "{0} - {1}"
        return txt.format(self.customer, self.ShipTo)

    class Meta:
        verbose_name = 'Ship To'
        verbose_name_plural = 'Ship To'


class Reps(models.Model):
    name = models.CharField(max_length=100, verbose_name='Rep Name', default='')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.name)

    class Meta:
        verbose_name = 'Representant'
        verbose_name_plural = 'Representant'

# Esta es la TABLA  orden que se usa para el tema de Labels
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False, blank=False, default='')
    shipto = models.ForeignKey(Destinos, on_delete=models.PROTECT, null=False, blank=False, default='')
    rep = models.ForeignKey(Reps, on_delete=models.PROTECT, null=False, blank=False, default='')
    Po_number = models.CharField(max_length=30, verbose_name='P.O Number', default='')
    So_number = models.CharField(max_length=30, verbose_name='S.O Number', default='')
    fecha = models.DateField(default=datetime.now, verbose_name='Create Date')
    Special_Inst = models.TextField(max_length=300, verbose_name='Special Inst.', default='')
    si_no = [('Y', 'Yes'), ('N', 'Not')]
    Procesed = models.CharField(max_length=1, choices=si_no, default='N')

    def __str__(self):
        txt = "{0}   {1}    {2}"
        return txt.format(self.customer, self.Po_number, self.So_number)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderDetails(models.Model):
    Orden = models.ForeignKey(Order, on_delete=models.PROTECT, null=False, blank=False, default='')
    Prod = models.ForeignKey(Product, verbose_name='Product ', on_delete=models.PROTECT, null=False, blank=False,
                             default='')
    Ordered_Qty = models.IntegerField(verbose_name='Ordered Qty ', null=False,  blank=False, default=0)
    QtySmallBox = models.IntegerField(verbose_name='Qty of Small Boxes', null=True, default=0)
    QtyBigBox = models.IntegerField(verbose_name='Qty of Master Boxes', null=True, default=0)

    def __str__(self):
        txt = "{0}   {1}    {2}"
        return txt.format(self.Orden, self.Prod, self.Ordered_Qty)

    class Meta:
        verbose_name = 'Order Details'
        verbose_name_plural = 'Order Details'


class BoxType2(models.Model):
    si_no = [('Y', 'Yes'), ('N', 'Not')]
    BoxType = models.IntegerField(verbose_name='Type of Box', null=False, blank=False, primary_key=True)
    cust_id = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False, blank=False, default='')
    QtySmallBox = models.IntegerField(verbose_name='Qty in SmallBox', null=False,  blank=False, default=0)
    SizeSmallBox = models.CharField(max_length=30, verbose_name='Size Small Box', default='8x6x4')
    QtySmallBox_inMaster = models.IntegerField(verbose_name='Qty of SmallBox in Master Box', null=False,
                                               blank=False, default=0)
    SizeMasterBox = models.CharField(max_length=30, verbose_name='Size Master Box', default='12x12x12')
    WeighMasterBox = models.IntegerField(verbose_name='Gross Weight', null=False, blank=False, default=0)
    NetWeighMasterBox = models.IntegerField(verbose_name='Net Weight', null=False, blank=False, default=0)

    def __str__(self):
        txt = "Type : {0} - QtyinSmallBox : {1} - Size ({2}) --- QtyinMasterBox : {3} - Size ({4})"
        return txt.format(self.BoxType,self.QtySmallBox,self.SizeSmallBox,self.QtySmallBox_inMaster,self.SizeMasterBox)

    class Meta:
        verbose_name = 'Box Type'
        verbose_name_plural = 'Box Type'


class Matrix(models.Model):
    si_no = [('S', 'Si'), ('N', 'No')]
    Customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False, blank=False, default='')
    Prod = models.ForeignKey(Product, on_delete=models.PROTECT, null=False, blank=False, default='')
    BoxType = models.ForeignKey(BoxType2, on_delete=models.PROTECT, null=False, blank=False, default='')
    ImgLabelSmallBox = models.CharField(max_length=30, verbose_name='Image barcode for Small Box', default='.png')
    ImgLabelMasterBox = models.CharField(max_length=30, verbose_name='Image barcode for Master Box ',default='.png')
    LabelAuxliar = models.CharField(max_length=1, choices=si_no, default='S')
    SKU = models.CharField(max_length=30, verbose_name='SKU', default='')
    EtiquetaMasterBox = models.CharField(max_length=1, choices=si_no, default='S')
    QtyEtiquetes = models.IntegerField(verbose_name='Qty de Etiquetas', null=False, blank=False,
                                               default=4)



    def __str__(self):
        txt = "{0}   {1}"
        return txt.format(self.Customer, self.Prod)

    class Meta:
        verbose_name = 'Matrix'
        verbose_name_plural = 'Matrix'


class WeightSheet(models.Model):
    Orderx = models.ForeignKey(Order, on_delete=models.PROTECT, null=False, blank=False, default='')
    BoxNumber = models.IntegerField(verbose_name='Qty Label for Small Box', null=False,  blank=False, default=0)
    Total_of_Items = models.IntegerField(verbose_name='Total of Items', null=False, blank=False, default=0)
    ProductName = models.CharField(max_length=100, verbose_name='Size Master Box', default='12x12x12')
    Weight = models.IntegerField(verbose_name='Gross Weight', null=False,  blank=False, default=0)
    Weight_Net = models.IntegerField(verbose_name='Net Weight', null=False, blank=False, default=0)
    Dimensions = models.CharField(max_length=30, verbose_name='Size Master Box', default='12x12x12')
    Barcode_image = models.CharField(max_length=100, verbose_name='Barcode_image', default='')
    SKU_p = models.CharField(max_length=100, verbose_name='Barcode_image', default='')
    PO_Num = models.CharField(max_length=100, verbose_name='Po Number', default='')
    Destino_final = models.CharField(max_length=100, verbose_name='Po Number', default='')
    color = models.CharField(max_length=100, verbose_name='Po Number', default='')

    def __str__(self):
        txt = "{0}   {1}"
        return txt.format(self.Orderx, self.BoxNumber)

    class Meta:
        verbose_name = 'WeightSheet'
        verbose_name_plural = 'WeightSheet'


class OrderDetailsInner(models.Model):
    Orden = models.ForeignKey(Order, on_delete=models.PROTECT, null=False, blank=False, default='')
    ProductName = models.CharField(max_length=100, verbose_name='Size Master Box', default='')
    Cantidad = models.IntegerField(verbose_name='Ordered Qty ', null=False,  blank=False, default=0)
    Archivo_imagen = models.CharField(max_length=100, verbose_name='Img File for label', default='')

    def __str__(self):
        txt = "{0}   {1}"
        return txt.format(self.Orden, self.ProductName)

    class Meta:
        verbose_name = 'Order Details Label'
        verbose_name_plural = 'Order Details Label'

# Aqui inicia
# el Modelo que se usa
# para el controL de contratistas y
# Pagos


class Contractor(models.Model):
    Name = models.CharField(max_length=100, verbose_name='Contractor Name', default='')
    email = models.EmailField(verbose_name='Email Contractor', default='')
    Phone = models.CharField(max_length=100, verbose_name='Phone Contractor', default='')

    def __str__(self):
        txt = "{0}"
        return txt.format(self.Name)

    class Meta:
        verbose_name = 'Contractor'
        verbose_name_plural = 'Contractors'


class Project(models.Model):
    Name = models.CharField(max_length=100, verbose_name='Contractor Name', default='')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.Name)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

class OrderContractor(models.Model):
    Project =  models.ForeignKey(Project, on_delete=models.PROTECT, null=False, blank=False, default='')
    Contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT, null=False, blank=False, default='')
    Qty_PS = models.IntegerField(default=500,verbose_name='Qty PS to use on this Order')
    Created_date = models.DateField(default=datetime.now, verbose_name=' Created Date')
    si_no = [('Y', 'Yes'), ('N', 'Not')]
    closed = models.CharField(max_length=1, choices=si_no, default='N')
    Special_Inst = models.TextField(max_length=300, verbose_name='Special Instructions.', default='')


    def __str__(self):
        txt = "{0}  "
        return txt.format(self.id)

    class Meta:
        verbose_name = 'Order Contractor'
        verbose_name_plural = 'Orders Contractor'


class OrderContractorDetail(models.Model):
    si_no = [('Y', 'Yes'), ('N', 'Not')]
    Orden = models.ForeignKey(OrderContractor, on_delete=models.PROTECT, null=False, blank=False, default='')
    Product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False, blank=False, default='')
    Qty_Req = models.IntegerField(verbose_name='Qty Required', null=False,  blank=False, default=0)
    Qty_Delivery = models.IntegerField(verbose_name='Qty Deliveried', null=False,  blank=False, default=0)
    Sellado = models.CharField(max_length=1, choices=si_no, default='N',verbose_name='2 Sticker')
    Barcode = models.CharField(max_length=1, choices=si_no, default='N')
    Pagado  = models.CharField(max_length=1, choices=si_no, default='N')
    En_QuickB = models.CharField(max_length=1, choices=si_no, default='N')
    fecha = models.DateField(verbose_name='Delivery Date',default=datetime.now,null=True, blank=True)
    Special_Inst = models.TextField(max_length=300, verbose_name='Special Instructions.', default='')
    Terminado = models.CharField(max_length=1, choices=si_no, default='N')
    fecha_de_pago = models.DateField(verbose_name='Paid Date', default=datetime.now, null=True, blank=True)
    fecha_quickbook = models.DateField(verbose_name='Quickbook Date', default=datetime.now, null=True, blank=True)
    user_update = models.CharField(max_length=50, verbose_name='User Name', default='')


    def __str__(self):
        txt = "Order {0}   - Detalle Num {1}"
        return txt.format(self.Orden,self.id)

    class Meta:
        verbose_name = 'OrderContractorDetail'
        verbose_name_plural = 'OrderContractorDetail'


class Liquidacion(models.Model):

    Orden = models.ForeignKey(OrderContractor, on_delete=models.PROTECT, null=False, blank=False, default='')
    Product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False, blank=False, default='')
    Qty_Delivery = models.IntegerField(verbose_name='Qty Deliveried', null=False,  blank=False, default=0)
    valor_unit = models.FloatField(default=0)
    valor_pagado = models.FloatField(default=0)
    fecha_liquidacion = models.DateField(verbose_name='Delivery Date',default=datetime.now,null=True, blank=True)
    Numero_Liquidacion = models.IntegerField(default=0)
    Contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT, null=False, blank=False, default='')


    def __str__(self):
        txt = "Order {0}   - Detalle Num {1}"
        return txt.format(self.Orden,self.id)

    class Meta:
        verbose_name = 'Liquidacion'
        verbose_name_plural = 'Liquidacion'



class Num_Liquidacion(models.Model):

    Numero_Liq = models.IntegerField()
    fecha_liquidacion = models.DateField(verbose_name='Payment Date', default=datetime.now, null=True, blank=True)
    Contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT, null=False, blank=False, default='')


    def __str__(self):
        txt = "{0} "
        return txt.format(self.Numero_Liq)


    class Meta:
        verbose_name = 'Num_Liquidacion'
        verbose_name_plural = 'Num_Liquidacion'

class OrderContractorDetail_Temp(models.Model):
    si_no = [('Y', 'Yes'), ('N', 'Not')]
    Orden = models.ForeignKey(OrderContractor, on_delete=models.PROTECT, null=False, blank=False, default='')
    Product = models.ForeignKey(Product, on_delete=models.PROTECT, null=False, blank=False, default='')
    Qty_Req = models.IntegerField(verbose_name='Qty Required', null=False,  blank=False, default=0)
    Qty_Delivery = models.IntegerField(verbose_name='Qty Deliveried', null=False,  blank=False, default=0)
    Sellado = models.CharField(max_length=1, choices=si_no, default='N')
    Barcode = models.CharField(max_length=1, choices=si_no, default='N')
    Pagado  = models.CharField(max_length=1, choices=si_no, default='N')
    fecha = models.DateField(verbose_name='Delivery Date',default=datetime.now,null=True, blank=True)
    Special_Inst = models.TextField(max_length=300, verbose_name='Special Instructions.', default='')
    Terminado = models.CharField(max_length=1, choices=si_no, default='N')
    fecha_de_pago = models.DateField(verbose_name='Paid Date', default=datetime.now, null=True, blank=True)
    Contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT, null=False, blank=False, default='')
