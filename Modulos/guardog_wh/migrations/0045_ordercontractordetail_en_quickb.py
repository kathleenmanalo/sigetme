# Generated by Django 3.1.7 on 2022-11-11 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guardog_wh', '0044_auto_20221110_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercontractordetail',
            name='En_QuickB',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'Not')], default='N', max_length=1),
        ),
    ]
