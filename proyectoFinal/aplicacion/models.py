
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    distribuidora = models.CharField(max_length=100)
    sinopsis = models.TextField() 
    actores = models.TextField()
    duracion = models.IntegerField()  # en minutos
    anio_estreno = models.IntegerField()
    poster = models.ImageField(upload_to='posters/')
    trailer_url = models.URLField(default='')
    CALIFICACION_CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    
    calificacion = models.PositiveIntegerField(choices=CALIFICACION_CHOICES)
    
    class Meta:
        ordering = ['titulo']
    def __str__(self):
        return self.titulo

class Serie(models.Model):
    titulo = models.CharField(max_length=200)
    temporadas = models.IntegerField()
    capitulos = models.IntegerField()
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    distribuidora = models.CharField(max_length=100)
    sinopsis = models.TextField()  
    actores = models.TextField()
    duracion = models.IntegerField()  # en minutos
    anio_estreno = models.IntegerField()
    poster = models.ImageField(upload_to='posters/')
    trailer_url = models.URLField(default='')
    CALIFICACION_CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    
    calificacion = models.PositiveIntegerField(choices=CALIFICACION_CHOICES)
    class Meta:
        ordering = ['titulo']
    def __str__(self):
        return self.titulo

class PeliculasTaquilleras(models.Model):
    titulo = models.CharField(max_length=200)
    
    NRO_PUESTO_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]
    
    puesto = models.PositiveIntegerField(choices=NRO_PUESTO_CHOICES)
    director = models.CharField(max_length=100)
    distribuidora = models.CharField(max_length=100)
    recaudacion_mundial = models.IntegerField()
    presupuesto = models.IntegerField()
    duracion = models.IntegerField()  # en minutos
    anio_estreno = models.IntegerField()
    poster = models.ImageField(upload_to='posters/')
    trailer_url = models.URLField(default='')
    
    class Meta:
        ordering = ['puesto']
    
    def __str__(self):
        return self.titulo

class Top10Series(models.Model):
    titulo = models.CharField(max_length=200)
    
    NRO_PUESTO_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]
    
    puesto = models.PositiveIntegerField(choices=NRO_PUESTO_CHOICES)
    genero = models.CharField(max_length=100)
    temporadas = models.IntegerField()
    capitulos = models.IntegerField()
    presupuesto = models.IntegerField()
    anio_estreno = models.IntegerField()
    poster = models.ImageField(upload_to='posters/')
    trailer_url = models.URLField(default='')
    
    class Meta:
        ordering = ['puesto']
    
    def __str__(self):
        return self.titulo

class Estreno(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    sinopsis = models.TextField() 
    duracion = models.IntegerField()  # en minutos
    poster = models.ImageField(upload_to='posters/')
    trailer_url = models.URLField(default='')
    fecha_estreno = models.DateField()
    
    TIPO_CHOICES = [
        ("Pelicula", "Película"),
        ("Serie", "Serie"),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    
    class Meta:
        ordering = ['fecha_estreno']
    
    def __str__(self):
        return self.titulo

class Reseña(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    TIPO_CHOICES = [
        ("Pelicula", "Película"),
        ("Serie", "Serie"),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    
    titulo_tipo = models.CharField(max_length=50)
    contenido = models.TextField() 
    
    CALIFICACION_CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    
    calificacion = models.PositiveIntegerField(choices=CALIFICACION_CHOICES)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['tipo']
    
    def __str__(self):
        return f'Reseña de {self.user} para {self.titulo_tipo}'

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
