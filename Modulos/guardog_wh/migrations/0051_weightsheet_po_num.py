# Generated by Django 3.1.7 on 2022-11-14 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guardog_wh', '0050_weightsheet_total_of_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='weightsheet',
            name='PO_Num',
            field=models.CharField(default='', max_length=100, verbose_name='Po Number'),
        ),
    ]
