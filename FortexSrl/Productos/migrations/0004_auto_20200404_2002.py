# Generated by Django 3.0.3 on 2020-04-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0003_auto_20200404_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproductos',
            name='temperatura',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproductos',
            name='tiempo_horno',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='temperatura',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='tiempo_horno',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
