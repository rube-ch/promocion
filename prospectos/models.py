from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from eventos.models import Evento

class Prospecto(models.Model):

    OPC_CARRERA = (
        ('ADM', 'ADMINISTRACION'),
        ('COM', 'COMUNICACION'),
        ('DER', 'DERECHO'),
        ('GST', 'GASTRONOMIA'),
        ('TUR', 'TURISMO'),
        ('OTR', 'OTRA'),
    )


    OPC_SINO = (
        ('S', 'SI'),
        ('N', 'NO'),
    )


    evento_id = models.ForeignKey(Evento, verbose_name='Evento')
    #escuela_id = models.ForeignKey()
    carrera = models.CharField('Carrera', max_length=3, choices=OPC_CARRERA)
    nombre = models.CharField('Primer nombre', max_length=40,
            help_text='Captura todo en MAYUSCULAS y sin acentos.'
    )
    nombre2 = models.CharField('Segundo nombre', max_length=40, blank=True)
    apaterno = models.CharField('Apellido paterno', max_length=40, blank=True)
    amaterno = models.CharField('Apellido materno', max_length=40, blank=True)
    telefono = models.CharField('Teléfono casa', blank=True, max_length=12,
            help_text='Captura el teléfono sin espacios ni guiones'
    )
    celular = models.CharField('Celular', blank=True, max_length=13,
            help_text='Captura el celular sin espacios ni guiones'
    )
    email = models.EmailField('Correo electrónico', blank=True)
    facebook = models.CharField('Facebook', blank=True, max_length=40)
    examen_buap = models.NullBooleanField('Examen BUAP', default=False)
    autor= models.ForeignKey(User, null=True, editable=False)
    creado = models.DateTimeField(auto_now_add=True, null=True)
    modificado = models.DateTimeField(auto_now=True, null=True)



class ProspectoForm(ModelForm):
    class Meta:
        model = Prospecto


# Create your models here.
