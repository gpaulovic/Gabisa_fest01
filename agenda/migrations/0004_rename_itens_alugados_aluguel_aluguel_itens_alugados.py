# Generated by Django 4.2 on 2023-04-28 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_remove_aluguel_itens_alugados_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluguel',
            old_name='itens_alugados_aluguel',
            new_name='itens_alugados',
        ),
    ]