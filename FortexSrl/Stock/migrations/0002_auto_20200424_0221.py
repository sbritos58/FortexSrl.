# Generated by Django 3.0.3 on 2020-04-24 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
