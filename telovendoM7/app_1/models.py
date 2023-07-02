from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User,AbstractUser
from django.utils.translation import gettext_lazy as _

# Manager
class PublicacionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

# Create your models here.
# REGIONES_CHOICES = [
#     ('XV', 'Region de Arica y Parinacota'),
#     ('I', 'Region de Tarapaca'),
#     ('II', 'Region de Antofagasta'),
#     ('III', 'Region de Atacama'),
#     ('IV', 'Region de Coquimbo'),
#     ('V', 'Region de Valparaiso'),
#     ('RM', 'Region de Metropolitana'),
#     ('VI', 'Region del Libertador General Bernardo O´Higgins'),
#     ('VII', 'Region del Maule'),
#     ('XVI', 'Region del Ñuble'),
#     ('VIII', 'Region del Biobio'),
#     ('IX', 'Region de La Araucania'),
#     ('XIV', 'Region de Los Rios'),
#     ('X', 'Region de Los Lagos'),
#     ('XI', 'Region de Aysen del General Carlos Ibañez del Campo'),
#     ('XII', 'Region de Magallanes y de la Antartica Chilena'),
# ]

PAGOS_CHOICES = [
    ('Efectivo', 'Efectivo'),
    ('Transferencia', 'Transferencia'),
    ('Crédito', 'Crédito'),
    ('Debito', 'Debito'),
    ('PayPal', 'PayPal'),
    ('Mach', 'Mach'),
]

VIA_CHOICES = [
    ('Telefono', 'Telefono'),
    ('E-mail', 'E-mail'),
    ('Web', 'Web'),
]

ESTADOS_CHOICES = [
    ('Pendiente', 'Pendiente'),
    ('En Preparación', 'En Preparación'),
    ('En Despacho', 'En Despacho'),
    ('Entregado', 'Entregado'),
]

class Cliente(AbstractUser):
    rut = models.CharField(max_length=10, blank=True)    
    first_name = models.CharField(max_length=30, blank=True)
    segundo_nombre = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    segundo_apellido = models.CharField(max_length=30, null=True, blank=True)
    direccion = models.CharField(max_length=250)
    telefono = models.IntegerField(null=True,blank=True)
    email = models.EmailField(max_length=50, blank=True, unique=True, verbose_name='email')
    # metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.DO_NOTHING)
    deleted = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'


    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class Direccion(models.Model):  
#     #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) --> dejaremos que la ID la genere Django por si solo
#     nombre = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     calle = models.CharField(max_length=100)
#     numero = models.IntegerField()
#     comuna = models.CharField(max_length=50)
#     religion = models.CharField(max_length=4, choices=REGIONES_CHOICES)
#     ciudad = models.CharField(max_length=30)
#     referencia = models.CharField(max_length=250, null=True)
#     deleted = models.BooleanField(default=False)
    
#     def delete(self, *args, **kwargs):
#         self.deleted = True
#         self.save()

#     @property
#     def str_nombre(self):
#         return f"{self.calle}, {self.comuna}, {self.region}, {self.ciudad}"
     
#     def __str__(self):
#         return self.str_nombre    

class Clasificacion(models.Model):
    nombre = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)
    
    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    id_clasificacion = models.ForeignKey(Clasificacion, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio_venta = models.IntegerField()
    deleted = models.BooleanField(default=False)
    
    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    #id = models.IntegerField(primary_key=True)
    #id_detallepedido = models.ForeignKey(DetallePedido, on_delete=models.CASCADE)
    idcliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, default=0)
    metodo_pago = models.CharField(max_length=15, choices=PAGOS_CHOICES, default='Crédito')
    # id_mediopedido = models.ForeignKey(DetallePedido.mediopedido, on_delete=models.DO_NOTHING, default=0)
    fecha_pedido = models.DateTimeField(default=timezone.now)
    mediopedido = models.CharField(max_length=15, choices=VIA_CHOICES, default='Web')
    estado = models.CharField(max_length=15, choices=ESTADOS_CHOICES, default='Pendiente')
    deleted = models.BooleanField(default=False)
    precio_total = models.IntegerField(default=0)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    @property
    def str_nombre(self):
        return f"Pedido N°: {self.id}"

    def __str__(self):
        return self.str_nombre

class DetallePedido(models.Model):
    id = models.AutoField(primary_key=True)
    idproducto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    idpedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    deleted = models.BooleanField(default=False)
    
    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    @property
    def str_nombre(self):
        return f"{self.id}, {self.idproducto}, {self.precio}"

    def __str__(self):
        return self.str_nombre