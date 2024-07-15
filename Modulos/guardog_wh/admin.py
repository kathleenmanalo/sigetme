from django.contrib import admin

# Register your models here.
from Modulos.guardog_wh.models import *
from user.models import *

admin.site.register (Estados)
admin.site.register (Cities)
admin.site.register (Customer)
admin.site.register (Product)
admin.site.register (Destinos)
admin.site.register (Reps)
admin.site.register (Order)
admin.site.register (OrderDetails)
admin.site.register (Matrix)
admin.site.register (BoxType2)
admin.site.register (WeightSheet)
admin.site.register (Contractor)
admin.site.register (Project)
admin.site.register (OrderContractor)
admin.site.register (OrderContractorDetail)
admin.site.register (rates)
admin.site.register (Num_Liquidacion)
admin.site.register (PSpray_Types)




# class detalle_ordernInline(admin.TabularInline):
#     model = OrderDetails
#
# class OrderAdmin(admin.ModelAdmin):
#     inlines = (detalle_ordernInline,)
#
# admin.site.register(Order, OrderAdmin)