from django.db import models

class Evento(models.Model):
    evento = models.IntegerField(primary_key=True)
    escuela = models.IntegerField('Clave de la escuela')
    nombre_evento = models.CharField(max_length=244)
    fecha = models.DateField('Fecha del evento',)
    #hora_inicio = models.TimeField('Hora de inicio')
    #hora_fin = models.TimeField('Hora de término')
    registros = models.IntegerField('Número de registros')
    
    def __unicode__(self):
        return nombre_evento
    
    class Meta:
        ordering = ('nombre_evento',)

# Create your models here.
