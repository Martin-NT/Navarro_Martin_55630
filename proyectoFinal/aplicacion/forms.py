from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PeliculaForm(forms.Form):
    titulo = forms.CharField(label = "Titulo",max_length=50,required=True)
    genero = forms.CharField(label = "Genero",max_length=50,required=True)
    director = forms.CharField(label = "Director",max_length=50,required=True)
    distribuidora = forms.CharField(label = "Distribuidora",max_length=50,required=True)  
    actores = forms.CharField(label = "Actores",required=True)
    sinopsis = forms.CharField(label = "Sinopsis",required=True)
    duracion = forms.IntegerField(label = "Duracion",required=True)
    anio_estreno = forms.IntegerField(label = "Año de Estreno",required=True)
    poster = forms.ImageField(label="Poster", required=True)
    trailer_url = forms.URLField(label = "Trailer",max_length=50,required=True)
    calificacion = forms.DecimalField(label = "Calificacion",required=True)

class SerieForm(forms.Form):
    titulo = forms.CharField(label = "Genero",max_length=50,required=True)
    temporadas = forms.IntegerField(label = "Temporadas",required=True)
    capitulos = forms.IntegerField(label = "Capitulos",required=True)
    genero = forms.CharField(label = "Genero",max_length=50,required=True)
    director = forms.CharField(label = "Genero",max_length=50,required=True)
    distribuidora = forms.CharField(label = "Genero",max_length=50,required=True)
    actores = forms.CharField(label = "Genero",required=True)
    sinopsis = forms.CharField(label = "Genero",required=True)
    duracion = forms.IntegerField(label = "Genero",required=True)
    anio_estreno = forms.IntegerField(label = "Genero",required=True)
    poster = forms.ImageField(label="Poster", required=True)
    trailer_url = forms.URLField(label = "Genero",max_length=50,required=True)
    calificacion = forms.DecimalField(label = "Genero",required=True)

from django import forms

class ReseñaForm(forms.Form):
    user = forms.CharField(label="Nombre de Usuario", required=True)
    TIPOS = [
        ("Pelicula", "Película"),
        ("Serie", "Serie")
    ]
    tipo = forms.ChoiceField(label="Opción Elegida", choices=TIPOS, required=True)
    titulo_tipo = forms.CharField(label="Nombre de Usuario", required=True,max_length=100)
    contenido = forms.CharField(label="Contenido", max_length=100, required=True)
    calificacion = forms.DecimalField(label="Calificación", required=True)
    fecha_publicacion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-3'}),
        required=True,
        label='Fecha de la Reseña'
    )

class EstrenoForm(forms.Form):
    titulo = forms.CharField(label = "Titulo",max_length=50,required=True)
    TIPO_CHOICES = [
        ("Pelicula", "Película"),
        ("Serie", "Serie"),
    ]
    tipo = forms.ChoiceField(label="Opción Elegida",choices=TIPO_CHOICES,required=True,
                        widget=forms.Select(attrs={'class': 'form-select mb-3'}))
    genero = forms.CharField(label = "Genero",max_length=50,required=True)
    director = forms.CharField(label = "Director",max_length=50,required=True)
    sinopsis = forms.CharField(label = "Sinopsis",required=True)
    duracion = forms.IntegerField(label = "Duracion",required=True)
    fecha_estreno = forms.IntegerField(label = "Fecha de Estreno",required=True)
    poster = forms.ImageField(label="Poster", required=True)
    trailer_url = forms.URLField(label = "Trailer",max_length=50,required=True)

class PeliculasTaquillerasForm(forms.Form):
    titulo = forms.CharField(label = "Titulo",max_length=50,required=True)
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
    puesto = forms.ChoiceField(choices=NRO_PUESTO_CHOICES)
    director = forms.CharField(label = "Director",max_length=50,required=True)
    duracion = forms.IntegerField(label = "Duracion",required=True)
    distribuidora = forms.CharField(label = "Genero",max_length=50,required=True)
    presupuesto = forms.IntegerField(required=True)
    recaudacion_mundial = forms.IntegerField(required=True)
    anio_estreno = forms.IntegerField(label = "Genero",required=True)
    poster = forms.ImageField(label="Poster", required=True)
    trailer_url = forms.URLField(label = "Trailer",max_length=50,required=True)


class Top10SeriesForm(forms.Form):
    titulo = forms.CharField(label = "Titulo",max_length=50,required=True)
    temporadas = forms.IntegerField(required=True)
    capitulos = forms.IntegerField(required=True)
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
    puesto = forms.ChoiceField(choices=NRO_PUESTO_CHOICES)
    director = forms.CharField(label = "Director",max_length=50,required=True)
    distribuidora = forms.CharField(label = "Genero",max_length=50,required=True)
    presupuesto = forms.IntegerField(required=True)
    recaudacion_mundial = forms.IntegerField(required=True)
    anio_estreno = forms.IntegerField(label = "Genero",required=True)
    poster = forms.ImageField(label="Poster", required=True)
    trailer_url = forms.URLField(label = "Trailer",max_length=50,required=True)

#Para Registro de Usuarios
class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Para Editar Usuarios
class UserEditForm(UserCreationForm):
    username = forms.CharField(label="Usuario", widget= forms.PasswordInput,required=False)
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

#Para agregar un Avatar 
class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)