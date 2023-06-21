from django.db import models
from django.utils import timezone
import uuid

# Manager
class PublicacionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

# Create your models here.
REGIONES_CHOICES = [
    ('XV', 'Region de Arica y Parinacota'),
    ('I', 'Region de Tarapaca'),
    ('II', 'Region de Antofagasta'),
    ('III', 'Region de Atacama'),
    ('IV', 'Region de Coquimbo'),
    ('V', 'Region de Valparaiso'),
    ('RM', 'Region de Metropolitana'),
    ('VI', 'Region del Libertador General Bernardo OHiggins'),
    ('VII', 'Region del Maule'),
    ('XVI', 'Region del Ñuble'),
    ('VIII', 'Region del Biobio'),
    ('IX', 'Region de La Araucania'),
    ('XIV', 'Region de Los Rios'),
    ('X', 'Region de Los Lagos'),
    ('XI', 'Region de Aysen del General Carlos Ibañez del Campo'),
    ('XII', 'Region de Magallanes y de la Antartica Chilena'),
]

PAGOS_CHOICES = [
    ('1', 'Efectivo'),
    ('2', 'Transferencia'),
    ('3', 'Crédito'),
    ('4', 'Debito'),
    ('5', 'PayPal'),
    ('6', 'Mach'),
]

VIA_CHOICES = [
    (1, 'Telefono'),
    (2, 'Email'),
    (3, 'Web'),
]

class Direccion(models.Model):  
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) --> dejaremos que la ID la genere Django por si solo
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=4, choices=REGIONES_CHOICES)
    ciudad = models.CharField(max_length=30)
    referencia = models.CharField(max_length=250)

    def __str__(self):
        return self.calle

class MetodoPago(models.Model):
    metodo_pago = models.CharField(max_length=4, choices=PAGOS_CHOICES, default=3)
    

class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rut = models.CharField(max_length=10)    
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, null=True)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30, null=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=50)
    # metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.DO_NOTHING)
    deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    def _str__(self):
        return self.rut

class Clasificacion(models.Model):
    nombre = models.CharField(max_length=50)
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    id_clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio_venta = models.IntegerField()
class DetallePedido(models.Model):
    id = models.AutoField(primary_key=True)
    idproducto = models.IntegerField(null=False)
    # idpedido = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    mediopedido = models.CharField(max_length=4, choices=VIA_CHOICES, default='3')

class Pedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_detallepedido = models.ForeignKey(DetallePedido, on_delete=models.DO_NOTHING, default=0)
    idcliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, default=0)
    pago_pedido = models.ForeignKey(MetodoPago, on_delete=models.DO_NOTHING, default=0)
    # id_mediopedido = models.ForeignKey(DetallePedido.mediopedido, on_delete=models.DO_NOTHING, default=0)
    fecha_pedido = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    def __str__(self):
        return self.id
    