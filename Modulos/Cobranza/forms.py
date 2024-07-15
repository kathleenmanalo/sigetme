from django.forms import *

from Modulos.guardog_wh.models import *
from sigetmeapp.models import *


class OrderForm(ModelForm):
	def __init__(self, *arg, **kwargs):
		super().__init__(*arg, **kwargs)
		for form in self.visible_fields():
			form.field.widget.attrs['class'] = 'form-control'
			form.field.widget.attrs['autocomplete'] = 'off'

	class Meta:
		model = Order
		fields = '__all__'




class OrderDetailsForm(ModelForm):
	def __init__(self, *arg, **kwargs):

		super().__init__(*arg, **kwargs)

		self.fields['Prod'].queryset = Product.objects.filter(menards='Y',dunams='Y',academy='Y')

		for form in self.visible_fields():
				form.field.widget.attrs['class'] = 'form-control'
				form.field.widget.attrs['autocomplete'] = 'off'
				if form.auto_id == 'id_Prod':
					a = 1111

	class Meta:
		model = OrderDetails
		fields = ['Prod','Ordered_Qty']
		# fields = '__all__'
		widgets = {
			# 'Prod':  Select(attrs={'class': 'form-control select2','style': 'width: 100%'}),
			'Ordered_Qty': NumberInput(
					attrs={'minlength': 1, 'maxlength': 2, 'required': True, 'type': 'number', 'class': 'form-control'}
				),

		}


class OrderContractorForm(ModelForm):
	def __init__(self, *arg, **kwargs):
		super().__init__(*arg, **kwargs)
		for form in self.visible_fields():
			form.field.widget.attrs['class'] = 'form-control'
			form.field.widget.attrs['autocomplete'] = 'off'

	class Meta:
		model = OrderContractor
		fields = '__all__'

# Aqui esta el formulario para actualizacion del detalla de la orden por cada producto

class OrderDetails_Cont_Form(ModelForm):
	def __init__(self, *arg, **kwargs):
		super().__init__(*arg, **kwargs)



		for form in self.visible_fields():
			form.field.widget.attrs['class'] = 'form-control'
			form.field.widget.attrs['autocomplete'] = 'off'


	class Meta:
		model = OrderContractorDetail
		fields = '__all__'

		# fields = ['Product', 'Qty_Req']


class OrderDetails_Cont_Form_Upd(ModelForm):
	def __init__(self, *arg, **kwargs):
		super().__init__(*arg, **kwargs)
		for form in self.visible_fields():
			form.field.widget.attrs['class'] = 'form-control'
			form.field.widget.attrs['autocomplete'] = 'off'
		self.fields['Orden'].widget.attrs['readonly'] = True
		self.fields['Product'].widget.attrs['readonly'] = True

	class Meta:
		model = OrderContractorDetail
		# fields = ['Product','Qty_Req','Qty_Delivery']
		fields = '__all__'
		widgets = {
			'Product': Select(attrs={
				'class': 'form-control',
				'style': 'width: 100%', 'readonly': True

				# antes no estaba disable sino readdonly y no funciono bien Mayo 13 2021
			}),
			'Orden': Select(attrs={
				'class': 'form-control',
				'style': 'width: 100%', 'readonly': True,'hidden': True,

				# antes no estaba disable sino readdonly y no funciono bien Mayo 13 2021
			}),
		}


class OrderDetails_Cont_Form_v2(ModelForm):
	def __init__(self, *arg, **kwargs):
		super().__init__(*arg, **kwargs)

		self.fields['Product'].queryset = Product.objects.filter(contractor='Y')

		for form in self.visible_fields():
			form.field.widget.attrs['class'] = 'form-control'
			form.field.widget.attrs['autocomplete'] = 'off'


	class Meta:
		model = OrderContractorDetail
		# fields = '__all__'
		fields = ['Product', 'Qty_Req','Barcode','Sellado','Special_Inst']