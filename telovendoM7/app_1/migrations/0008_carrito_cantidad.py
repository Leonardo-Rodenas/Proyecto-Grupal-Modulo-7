# Generated by Django 4.2.2 on 2023-07-07 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0007_carrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
