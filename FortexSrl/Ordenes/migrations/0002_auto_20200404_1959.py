# Generated by Django 3.0.3 on 2020-04-04 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ordenes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenes',
            name='asignado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Asignado', to=settings.AUTH_USER_MODEL, verbose_name='Asignado a '),
        ),
        migrations.AddField(
            model_name='ordenes',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.Productos', verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='historicalordenes',
            name='asignado',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Asignado a '),
        ),
        migrations.AddField(
            model_name='historicalordenes',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalordenes',
            name='producto',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Productos.Productos', verbose_name='Producto'),
        ),
    ]
