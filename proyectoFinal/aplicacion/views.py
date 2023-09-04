from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Pelicula, Serie, PeliculasTaquilleras, Reseña, Estreno, Top10Series, Avatar
from .forms import PeliculaForm, SerieForm, ReseñaForm, EstrenoForm, PeliculasTaquillerasForm, Top10SeriesForm, AvatarFormulario, RegistroUsuariosForm, UserEditForm

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    return render(request, "aplicacion/inicio.html")

def acerca_de(request):
    return render(request, 'aplicacion/acerca_de.html')

#def peliculas(request):
    #contexto = {'peliculas': Pelicula.objects.all()}
    #return render(request, 'aplicacion/peliculas.html', contexto)

#def series(request):
    #contexto = {'series': Serie.objects.all()}
    #return render(request, 'aplicacion/series.html', contexto)

@login_required 
def top10(request):
    return render(request, 'aplicacion/top10.html')

@login_required 
def buscar(request):
    return render(request, 'aplicacion/buscar.html')

@login_required 
def buscar_peliculas(request):
    return render(request, 'aplicacion/buscar_peliculas.html')

@login_required 
def buscar_series(request):
    return render(request, 'aplicacion/buscar_series.html')

@login_required 
def buscar_estrenos(request):
    return render(request, 'aplicacion/buscar_estrenos.html')

#Buscar Peliculas
@login_required 
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        peliculas = Pelicula.objects.filter(titulo__icontains=patron)
        contexto = {'peliculas': peliculas,  'titulo': f'listado de peliculas que tiene como patron "{patron}"'}
        return render(request, "aplicacion/peliculas.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

#Buscar Series
@login_required 
def buscar3(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        series = Serie.objects.filter(titulo__icontains=patron)
        contexto = {'series': series,  'titulo': f'listado de series que tiene como patron "{patron}"'}
        return render(request, "aplicacion/series.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

#Buscar Estrenos
@login_required  
def buscar4(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        estrenos = Estreno.objects.filter(titulo__icontains=patron)
        contexto = {'estrenos': estrenos,  'titulo': f'listado de estrenos que tiene como patron "{patron}"'}
        return render(request, "aplicacion/estrenos.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

@login_required 
def agregar(request):
    return render(request, 'aplicacion/agregar.html')

@login_required 
def agregar_peliculas(request):
    return render(request, 'aplicacion/pelicula_form.html')

@login_required 
def agregar_series(request):
    return render(request, 'aplicacion/serie_form.html')

@login_required 
def agregar_estrenos(request):
    return render(request, 'aplicacion/estreno_form.html')

@login_required 
def agregar_reseñas(request):
    return render(request, 'aplicacion/reseña_form.html')

@login_required 
def agregar_peliculas_taquilleras(request):
    return render(request, 'aplicacion/peliculas_taquilleras_form.html')

@login_required 
def agregar_top10_series(request):
    return render(request, 'aplicacion/top10_series_form.html')

#Agregar Peliculas
@login_required 
def peliculaForm(request):
    if request.method == "POST":
        miForm = PeliculaForm(request.POST)
        if miForm.is_valid():
            pelicula_titulo = miForm.cleaned_data.get('titulo').title()
            pelicula_genero = miForm.cleaned_data.get('genero').title()
            pelicula_director = miForm.cleaned_data.get('director').title()
            pelicula_distribuidora = miForm.cleaned_data.get('distribuidora').title()
            pelicula_actores = miForm.cleaned_data.get('actores').title()
            pelicula_sinopsis = miForm.cleaned_data.get('sinopsis')
            pelicula_anio_estreno = miForm.cleaned_data.get('anio estreno')
            pelicula_poster = miForm.cleaned_data.get('poster')
            pelicula_trailer_url = miForm.cleaned_data.get('trailer url')
            pelicula_calificacion = miForm.cleaned_data.get('calificacion')
            pelicula = Pelicula(titulo = pelicula_titulo,
                                genero = pelicula_genero, 
                                director = pelicula_director,
                                distribuidora = pelicula_distribuidora,
                                actores = pelicula_actores,
                                sinopsis = pelicula_sinopsis,
                                anio_estreno = pelicula_anio_estreno,
                                poster = pelicula_poster,
                                trailer_url = pelicula_trailer_url, 
                                calificacion = pelicula_calificacion)
            pelicula.save()
            messages.success(request, 'Pelicula agregada exitosamente.')
            return redirect(reverse_lazy('pelicula_form'))
    else:
        miForm = PeliculaForm()

    return render(request, "aplicacion/pelicula_form.html", {"form":miForm})

#Agregar Series
@login_required 
def serieForm(request):
    if request.method == "POST":
        miForm = SerieForm(request.POST)
        if miForm.is_valid():
            serie_titulo = miForm.cleaned_data.get('titulo').title()
            serie_genero = miForm.cleaned_data.get('genero').title()
            serie_temporadas= miForm.cleaned_data.get('temporadas')
            serie_capitulos = miForm.cleaned_data.get('capitulos')
            serie_director = miForm.cleaned_data.get('director').title()
            serie_distribuidora = miForm.cleaned_data.get('distribuidora').title()
            serie_actores = miForm.cleaned_data.get('actores').title()
            serie_sinopsis = miForm.cleaned_data.get('sinopsis')
            serie_anio_estreno = miForm.cleaned_data.get('anio estreno')
            serie_poster = miForm.cleaned_data.get('poster')
            serie_trailer_url = miForm.cleaned_data.get('trailer url')
            serie_calificacion = miForm.cleaned_data.get('calificacion')
            serie = Pelicula(titulo = serie_titulo,
                                genero = serie_genero, 
                                temporadas = serie_temporadas,
                                capitulos = serie_capitulos,
                                director = serie_director,
                                distribuidora = serie_distribuidora,
                                actores = serie_actores,
                                sinopsis = serie_sinopsis,
                                anio_estreno = serie_anio_estreno,
                                poster = serie_poster,
                                trailer_url = serie_trailer_url, 
                                calificacion = serie_calificacion)
            serie.save()
            messages.success(request, 'Serie agregada exitosamente.')
            return redirect(reverse_lazy('serie_form'))
    else:
        miForm = SerieForm()

    return render(request, "aplicacion/serie_form.html", {"form":miForm})

#Agregar Estrenos
@login_required 
def estrenoForm(request):
    if request.method == "POST":
        miForm = EstrenoForm(request.POST)
        if miForm.is_valid():
            estreno_titulo = miForm.cleaned_data.get('titulo').title()
            estreno_tipo = miForm.cleaned_data.get('estado')
            estreno_fecha_estreno = miForm.cleaned_data.get('fecha estreno')
            estreno_sinopsis = miForm.cleaned_data.get('sinopsis')
            estreno_poster = miForm.cleaned_data.get('poster')
            estreno_trailer_url = miForm.cleaned_data.get('trailer url')
            estreno = Estreno(titulo = estreno_titulo, 
                                tipo = estreno_tipo,
                                sinopsis = estreno_sinopsis,
                                fecha_estreno = estreno_fecha_estreno,
                                poster = estreno_poster,
                                trailer_url = estreno_trailer_url)
            estreno.save()
            messages.success(request, 'Estreno agregado exitosamente.')
            return redirect(reverse_lazy('estreno_form'))
    else:
        miForm = EstrenoForm()

    return render(request, "aplicacion/estreno_form.html", {"form":miForm})

#Agregar Reseñas
@login_required 
def reseñaForm(request):
    if request.method == "POST":
        miForm = ReseñaForm(request.POST)
        if miForm.is_valid():
            resenia_usuario = miForm.cleaned_data.get('usuario')
            resenia_tipo = miForm.cleaned_data.get('tipo')
            resenia_contenido = miForm.cleaned_data.get('contenido')
            resenia_calificacion = miForm.cleaned_data.get('calificacion')
            resenia_fecha_publicacion = miForm.cleaned_data.get('fecha publicacion')
            resenia = Reseña(usuario = resenia_usuario,
                            tipo = resenia_tipo,
                            contenido = resenia_contenido,
                            calificacion = resenia_calificacion,
                            fecha_publicacion = resenia_fecha_publicacion)
            resenia.save()
            messages.success(request, 'Reseña agregada exitosamente.')
            return redirect(reverse_lazy('reseña_form'))
    else:
        miForm = ReseñaForm()

    return render(request, "aplicacion/reseña_form.html", {"form":miForm})

#Agregar Peliculas Taquilleras
@login_required 
def peliculasTaquillerasForm(request):
    if request.method == "POST":
        miForm = PeliculasTaquillerasForm(request.POST)
        if miForm.is_valid():
            peliculaT_titulo = miForm.cleaned_data.get('titulo').title()
            peliculaT_duracion = miForm.cleaned_data.get('duracion')
            peliculaT_puesto = miForm.cleaned_data.get('puesto').title()
            peliculaT_director = miForm.cleaned_data.get('director').title()
            peliculaT_distribuidora = miForm.cleaned_data.get('distribuidora').title()
            peliculaT_recaudacion_mundial = miForm.cleaned_data.get('recaudacion mundial')
            peliculaT_presupuesto = miForm.cleaned_data.get('presupuesto')
            peliculaT_anio_estreno = miForm.cleaned_data.get('anio estreno')
            peliculaT_poster = miForm.cleaned_data.get('poster')
            peliculaT_trailer_url = miForm.cleaned_data.get('trailer url')
            peliculaT = Pelicula(titulo = peliculaT_titulo,
                                director = peliculaT_director,
                                distribuidora = peliculaT_distribuidora,
                                recaudacion_mundial = peliculaT_recaudacion_mundial,
                                presupuesto = peliculaT_presupuesto,
                                anio_estreno = peliculaT_anio_estreno,
                                poster = peliculaT_poster,
                                trailer_url = peliculaT_trailer_url,
                                duracion = peliculaT_duracion,
                                puesto = peliculaT_puesto)
            peliculaT.save()
            return redirect(reverse_lazy('peliculas_taquilleras_form'))
    else:
        miForm = PeliculasTaquillerasForm()

    return render(request, "aplicacion/peliculas_taquilleras_form.html", {"form":miForm})

#Agregar Series
@login_required 
def top10SerieForm(request):
    if request.method == "POST":
        miForm = Top10Series(request.POST)
        if miForm.is_valid():
            top_serie_titulo = miForm.cleaned_data.get('titulo').title()
            top_serie_genero = miForm.cleaned_data.get('genero').title()
            top_serie_temporadas= miForm.cleaned_data.get('temporadas')
            top_serie_capitulos = miForm.cleaned_data.get('capitulos')
            top_serie_presupuesto = miForm.cleaned_data.get('presupuesto')
            top_serie_anio_estreno = miForm.cleaned_data.get('anio estreno')
            top_serie_poster = miForm.cleaned_data.get('poster')
            top_serie_trailer_url = miForm.cleaned_data.get('trailer url')
            top_serie = Pelicula(titulo = top_serie_titulo,
                                genero = top_serie_genero, 
                                temporadas = top_serie_temporadas,
                                capitulos = top_serie_capitulos,
                                presupuesto = top_serie_presupuesto,
                                anio_estreno = top_serie_anio_estreno,
                                poster = top_serie_poster,
                                trailer_url = top_serie_trailer_url)
            top_serie.save()
            messages.success(request, 'Top 10 Serie agregada exitosamente.')
            return redirect(reverse_lazy('top10_series_form'))
    else:
        miForm = Top10Series()

    return render(request, "aplicacion/top10_series_form.html", {"form":miForm})

#----------------------- Class Based View -----------------------
# LoginRequiredMixin --> Mixin

#Lista de Peliculas
class PeliculaList(LoginRequiredMixin, ListView):
    model = Pelicula
    context_object_name = 'peliculas'
    template_name = 'aplicacion/pelicula_list.html'

#Crear Pelicula
class PeliculaCreate(LoginRequiredMixin, CreateView):
    model = Pelicula
    template_name = 'aplicacion/pelicula_form.html'
    fields = ['titulo', 'genero', 'director', 'distribuidora', 'actores', 'sinopsis', 'duracion', 
            'anio_estreno', 'poster', 'trailer_url', 'calificacion']
    success_url = reverse_lazy('peliculas')

#Modificar Pelicula
class PeliculaUpdate(LoginRequiredMixin, UpdateView):
    model = Pelicula
    template_name = 'aplicacion/pelicula_form.html'
    fields = ['titulo', 'genero', 'director', 'distribuidora', 'actores', 'sinopsis', 'duracion', 
            'anio_estreno', 'poster', 'trailer_url', 'calificacion']
    success_url = reverse_lazy('peliculas')

#Eliminar Pelicula
class PeliculaDelete(LoginRequiredMixin, DeleteView):
    model = Pelicula
    success_url = reverse_lazy('peliculas')

#----------------------------------------------------------------------------------------------------------------------------------------
#Lista de Series
class SerieList(LoginRequiredMixin, ListView):
    model = Serie
    context_object_name = 'series'
    template_name = 'aplicacion/serie_list.html'

#Crear Serie
class SerieCreate(LoginRequiredMixin, CreateView):
    model = Serie
    template_name = 'aplicacion/serie_form.html'
    fields = ['titulo', 'temporadas', 'capitulos', 'genero', 'director', 'distribuidora', 'actores', 'sinopsis', 'duracion', 
            'anio_estreno', 'poster', 'trailer_url', 'calificacion']
    success_url = reverse_lazy('series')

#Modificar Serie
class SerieUpdate(LoginRequiredMixin, UpdateView):
    model = Serie
    template_name = 'aplicacion/serie_list.html'
    fields = ['titulo', 'temporadas', 'capitulos','genero', 'director', 'distribuidora', 'actores', 'sinopsis', 'duracion', 
            'anio_estreno', 'poster', 'trailer_url', 'calificacion']
    success_url = reverse_lazy('series')
    template_name = 'aplicacion/serie_form.html'

#Eliminar Serie
class SerieDelete(LoginRequiredMixin, DeleteView):
    model = Serie
    success_url = reverse_lazy('series')
    template_name = 'aplicacion/serie_confirm_delete.html'

#----------------------------------------------------------------------------------------------------------------------------------------
#Lista de Estrenos
class EstrenoList(LoginRequiredMixin, ListView):
    model = Estreno
    context_object_name = 'estrenos'
    template_name = 'aplicacion/estreno_list.html'

#Crear Estreno 
class EstrenoCreate(LoginRequiredMixin, CreateView):
    model = Estreno
    template_name = 'aplicacion/estreno_form.html'
    fields = ['titulo', 'tipo', 'genero', 'director', 'duracion', 'fecha_estreno', 'sinopsis', 'poster', 'trailer_url']
    success_url = reverse_lazy('estrenos')

#Modificar Estreno
class EstrenoUpdate(LoginRequiredMixin, UpdateView):
    model = Estreno
    template_name = 'aplicacion/estreno_form.html'
    fields = ['titulo', 'tipo', 'genero', 'director', 'duracion', 'fecha_estreno', 'sinopsis', 'poster', 'trailer_url']
    success_url = reverse_lazy('estrenos')
    template_name = 'aplicacion/estreno_form.html'

#Eliminar Estreno
class EstrenoDelete(LoginRequiredMixin, DeleteView):
    model = Estreno
    success_url = reverse_lazy('estrenos')
    template_name = 'aplicacion/estreno_confirm_delete.html'

#----------------------------------------------------------------------------------------------------------------------------------------
#Lista de Peliculas Taquilleras
class PeliculasTaquillerasList(LoginRequiredMixin, ListView):
    model = PeliculasTaquilleras
    context_object_name = 'peliculas_taquilleras'
    template_name = 'aplicacion/peliculas_taquilleras_list.html'

#Crear Pelicula Taquillera
class PeliculasTaquillerasCreate(LoginRequiredMixin, CreateView):
    model = PeliculasTaquilleras
    fields = ['titulo', 'puesto', 'director', 'distribuidora', 'recaudacion_mundial', 'presupuesto','anio_estreno', 'poster', 'trailer_url', 'duracion']
    success_url = reverse_lazy('peliculas_taquilleras')
    template_name = 'aplicacion/peliculas_taquilleras_form.html'

#Modificar Pelicula Taquillera
class PeliculasTaquillerasUpdate(LoginRequiredMixin, UpdateView):
    model = PeliculasTaquilleras
    fields = ['titulo', 'puesto', 'director', 'distribuidora', 'recaudacion_mundial', 'presupuesto','anio_estreno', 'poster', 'trailer_url', 'duracion']
    success_url = reverse_lazy('peliculas_taquilleras')
    template_name = 'aplicacion/peliculas_taquilleras_form.html'

#Eliminar Pelicula Taquillera
class PeliculasTaquillerasDelete(LoginRequiredMixin, DeleteView):
    model = PeliculasTaquilleras
    success_url = reverse_lazy('peliculas_taquilleras')
    template_name = 'aplicacion/peliculas_taquilleras_confirm_delete.html'

#----------------------------------------------------------------------------------------------------------------------------------------
#Lista de Top 10 Series
class Top10SeriesList(LoginRequiredMixin, ListView):
    model = Top10Series
    context_object_name = 'top10_series'
    template_name = 'aplicacion/top10_series_list.html'

#Crear Serie
class Top10SeriesCreate(LoginRequiredMixin, CreateView):
    model = Top10Series
    fields = ['titulo', 'puesto', 'genero','temporadas', 'capitulos', 'presupuesto', 'anio_estreno', 'poster', 'trailer_url']
    success_url = reverse_lazy('top10_series')
    template_name = 'aplicacion/top10_series_form.html'

#Modificar Serie
class Top10SeriesUpdate(LoginRequiredMixin, UpdateView):
    model = Top10Series
    fields = ['titulo', 'puesto', 'genero','temporadas', 'capitulos', 'presupuesto', 'anio_estreno', 'poster', 'trailer_url']
    success_url = reverse_lazy('top10_series')
    template_name = 'aplicacion/top10_series_form.html'

#Eliminar Serie
class Top10SeriesDelete(LoginRequiredMixin, DeleteView):
    model = Top10Series
    success_url = reverse_lazy('top10_series')
    template_name = 'aplicacion/top10_serie_confirm_delete.html'

#----------------------------------------------------------------------------------------------------------------------------------------
#Lista de Reseñas
class ReseñaList(LoginRequiredMixin, ListView):
    model = Reseña
    context_object_name = 'resenias'
    template_name = 'aplicacion/reseña_list.html'

#Crear Reseña
class ReseñaCreate(LoginRequiredMixin, CreateView):
    model = Reseña
    fields = ['user', 'tipo', 'titulo_tipo', 'contenido', 'calificacion']
    success_url = reverse_lazy('resenias') 
    template_name = 'aplicacion/reseña_form.html'


#Modificar Reseña
class ReseñaUpdate(LoginRequiredMixin, UpdateView):
    model = Reseña
    fields = ['user', 'tipo', 'titulo_tipo', 'contenido', 'calificacion']
    success_url = reverse_lazy('resenias')
    template_name = 'aplicacion/reseña_form.html'

#Eliminar Reseña
class ReseñaDelete(LoginRequiredMixin, DeleteView):
    model = Reseña
    success_url = reverse_lazy('resenias')

#----------------------------------------------------------------------------------------------------------------------------------------
#Para Iniciar Sesion
def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "aplicacion/media/avatares/default.jpg"
                finally:
                    request.session["avatar"] = avatar
                return render(request, "aplicacion/inicio.html")
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm})    

#----------------------------------------------------------------------------------------------------------------------------------------
#Para Registrarse
def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            #messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return render(request, "aplicacion/inicio.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm}) 

#----------------------------------------------------------------------------------------------------------------------------------------
@login_required 
def perfil(request):
    return render(request, 'aplicacion/perfil.html')
#----------------------------------------------------------------------------------------------------------------------------------------
#Para Ver Perfil
@login_required
def verPerfil(request):
    usuario = request.user  # Obtiene el usuario autenticado
    
    return render(request, "aplicacion/verPerfil.html", {'usuario': usuario})
#----------------------------------------------------------------------------------------------------------------------------------------
#Para Editar Perfil
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.username = form.cleaned_data.get('username')
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"aplicacion/inicio.html")
        else:
            return render(request,"aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})

#----------------------------------------------------------------------------------------------------------------------------------------
#Para Agregar Avatar
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) # Diferente a los forms tradicionales
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            # ____ Guardar el nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___ Hago que la url de la imagen viaje en el request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/verPerfil.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form })