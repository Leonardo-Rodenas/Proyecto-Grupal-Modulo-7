# Generated by Django 4.2.2 on 2023-07-03 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_pedido_modificable_pedido_pedido_staff_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='modificable',
            new_name='is_modificable',
        ),
    ]
