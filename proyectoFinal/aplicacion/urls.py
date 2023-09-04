from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    #Urls propias de la aplicacion 
    path('', inicio, name="inicio" ),
    path('acerca_de/', acerca_de, name="acerca_de"),
    
    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
    path('registro/', register, name="registro" ),

    path('perfil/', perfil, name="perfil" ),
    path('ver_perfil/', verPerfil, name="ver_perfil" ),
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),
    
    path('agregar/', agregar, name="agregar"),
    path('buscar/', buscar, name="buscar"),
    
    path('buscar_peliculas/', buscar_peliculas, name="buscar_peliculas"),
    path('buscar_series/', buscar_series, name="buscar_series"),
    path('buscar_estrenos/', buscar_estrenos, name="buscar_estrenos"),

    
    path('buscar2/', buscar2, name="buscar2"), #Buscar Peliculas
    path('buscar3/', buscar3, name="buscar3"), #Buscar Series
    path('buscar4/', buscar4, name="buscar4"), #Buscar Actores

    
    path('peliculas/', PeliculaList.as_view(), name="peliculas"),
    path('create_pelicula/', PeliculaCreate.as_view(), name="create_pelicula" ),
    path('update_pelicula/<int:pk>/', PeliculaUpdate.as_view(), name="update_pelicula" ),
    path('delete_pelicula/<int:pk>/', PeliculaDelete.as_view(), name="delete_pelicula" ),
    
    path('series/', SerieList.as_view(), name="series"),
    path('create_serie/', SerieCreate.as_view(), name="create_serie" ),
    path('update_serie/<int:pk>/', SerieUpdate.as_view(), name="update_serie" ),
    path('delete_serie/<int:pk>/', SerieDelete.as_view(), name="delete_serie" ),
    
    path('estrenos/', EstrenoList.as_view(), name="estrenos"),
    path('create_estreno/', EstrenoCreate.as_view(), name="create_estreno" ),
    path('update_estreno/<int:pk>/', EstrenoUpdate.as_view(), name="update_estreno" ),
    path('delete_estreno/<int:pk>/', EstrenoDelete.as_view(), name="delete_estreno" ),
    
    path('resenias/', ReseñaList.as_view(), name="resenias"),
    path('create_resenia/', ReseñaCreate.as_view(), name="create_resenia" ),
    path('update_resenia/<int:pk>/', ReseñaUpdate.as_view(), name="update_resenia" ),
    path('delete_resenia/<int:pk>/', ReseñaDelete.as_view(), name="delete_resenia" ),
    
    path('top10/', top10, name="top10"),
    
    path('peliculas_taquilleras/', PeliculasTaquillerasList.as_view(), name="peliculas_taquilleras"),
    path('create_peliculas_taquilleras/', PeliculasTaquillerasCreate.as_view(), name="create_peliculas_taquilleras" ),
    path('update_peliculas_taquilleras/<int:pk>/', PeliculasTaquillerasUpdate.as_view(), name="update_peliculas_taquilleras" ),
    path('delete_peliculas_taquilleras/<int:pk>/', PeliculasTaquillerasDelete.as_view(), name="delete_peliculas_taquilleras" ),
    
    path('top10_series/', Top10SeriesList.as_view(), name="top10_series"),
    path('create_top10_series/', Top10SeriesCreate.as_view(), name="create_top10_series" ),
    path('update_top10_series/<int:pk>/', Top10SeriesUpdate.as_view(), name="update_top10_series" ),
    path('delete_top10_series<int:pk>/', Top10SeriesDelete.as_view(), name="delete_top10_series" ),
]
