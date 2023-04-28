# Generated by Django 4.2 on 2023-04-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_remove_item_preco_alter_aluguel_itens_alugados'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluguel',
            name='itens_alugados',
        ),
        migrations.AddField(
            model_name='aluguel',
            name='itens_alugados_aluguel',
            field=models.ManyToManyField(blank=True, related_name='alugueis_relacionados', to='agenda.item'),
        ),
        migrations.AddField(
            model_name='item',
            name='aluguel',
            field=models.ManyToManyField(related_name='itens_alugados_item', to='agenda.aluguel'),
        ),
    ]