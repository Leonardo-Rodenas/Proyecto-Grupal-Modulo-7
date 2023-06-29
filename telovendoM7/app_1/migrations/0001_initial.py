# Generated by Django 4.2.2 on 2023-06-29 05:21

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rut', models.CharField(blank=True, max_length=10)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('segundo_nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('segundo_apellido', models.CharField(blank=True, max_length=30, null=True)),
                ('direccion', models.CharField(max_length=250)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('deleted', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('precio_venta', models.IntegerField()),
                ('deleted', models.BooleanField(default=False)),
                ('id_clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.clasificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo_pago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Transferencia', 'Transferencia'), ('Crédito', 'Crédito'), ('Debito', 'Debito'), ('PayPal', 'PayPal'), ('Mach', 'Mach')], default='Crédito', max_length=15)),
                ('fecha_pedido', models.DateTimeField(default=django.utils.timezone.now)),
                ('mediopedido', models.CharField(choices=[('Telefono', 'Telefono'), ('E-mail', 'E-mail'), ('Web', 'Web')], default='Web', max_length=15)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Preparación', 'En Preparación'), ('En Despacho', 'En Despacho'), ('Entregado', 'Entregado')], default='Pendiente', max_length=15)),
                ('deleted', models.BooleanField(default=False)),
                ('precio_total', models.IntegerField(default=0)),
                ('idcliente', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('deleted', models.BooleanField(default=False)),
                ('idpedido', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_1.pedido')),
                ('idproducto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_1.producto')),
            ],
        ),
    ]
