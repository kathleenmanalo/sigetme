# Generated by Django 3.1.7 on 2022-09-25 20:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guardog_wh', '0011_remove_ordercontractor_pago_date'),
    ]

    operations = [

        migrations.AddField(
            model_name='ordercontractor',
            name='Created_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Date'),
        ),

    ]