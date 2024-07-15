# Generated by Django 3.1.7 on 2022-10-03 03:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guardog_wh', '0039_liquidacion_numero_liquidacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquidacion',
            name='Contractor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='guardog_wh.contractor'),
        ),
        migrations.CreateModel(
            name='OrderContractorDetail_Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qty_Req', models.IntegerField(default=0, verbose_name='Qty Required')),
                ('Qty_Delivery', models.IntegerField(default=0, verbose_name='Qty Deliveried')),
                ('Sellado', models.CharField(choices=[('Y', 'Yes'), ('N', 'Not')], default='N', max_length=1)),
                ('Barcode', models.CharField(choices=[('Y', 'Yes'), ('N', 'Not')], default='N', max_length=1)),
                ('Pagado', models.CharField(choices=[('Y', 'Yes'), ('N', 'Not')], default='N', max_length=1)),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Delivery Date')),
                ('Special_Inst', models.TextField(default='', max_length=300, verbose_name='Special Instructions.')),
                ('Terminado', models.CharField(choices=[('Y', 'Yes'), ('N', 'Not')], default='N', max_length=1)),
                ('fecha_de_pago', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Paid Date')),
                ('Contractor', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='guardog_wh.contractor')),
                ('Orden', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='guardog_wh.ordercontractor')),
                ('Product', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='guardog_wh.product')),
            ],
        ),
    ]
