# Generated by Django 3.1.7 on 2022-09-25 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guardog_wh', '0006_auto_20220919_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercontractor',
            name='Special_Inst',
            field=models.TextField(default='', max_length=300, verbose_name='Special Instructions.'),
        ),
        migrations.AddField(
            model_name='ordercontractor',
            name='closed',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='ordercontractor',
            name='paied',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], default='N', max_length=1),
        ),
    ]
