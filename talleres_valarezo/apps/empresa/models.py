from django.db import models

# Create your models here.
class Empresa (models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=255)
	logo = models.ImageField(upload_to='empresa')
	nacimiento = models.CharField(max_length=255)
	mision = models.CharField(max_length=255)
	vision = models.CharField(max_length=255)
	img_mision = models.ImageField(upload_to='empresa')
	img_vision = models.ImageField(upload_to='empresa')
	telef_convencional = models.CharField(max_length=10)
	telef_celular = models.CharField(max_length=10)
	email = models.EmailField()
	direccion = models.CharField(max_length=155)

	def __unicode__(self):
		#return "%s %s" % (self.nombre, self.descripcion)
		return self.nombre

class Servicio (models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=155)
	imagen = models.ImageField(upload_to='servicios')

	def __unicode__(self):
		return self.nombre

class Contacto (models.Model):
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	email = models.EmailField()
	informacion = models.CharField(max_length=1000)
	fecha = models.DateField(auto_now_add=True)
	revisado = models.BooleanField(default=False)
	atendido = models.BooleanField(default=False)

	def __unicode__(self):
		return "%s %s %s" %(self.nombre, self.apellidos, self.email)