# Generated by Django 4.2 on 2023-04-18 14:49

from django.db import migrations
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=localflavor.br.models.BRCPFField(max_length=14, unique=True, verbose_name='CPF'),
        ),
    ]
