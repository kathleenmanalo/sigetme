# Generated by Django 3.1.7 on 2023-03-22 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guardog_wh', '0055_weightsheet_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercontractordetail',
            name='Sellado',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'Not')], default='N', max_length=1, verbose_name='2 Sticker'),
        ),
    ]
