# Generated by Django 3.1.7 on 2022-10-02 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guardog_wh', '0034_auto_20221002_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercontractordetail',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Delivery Date'),
        ),

    ]
