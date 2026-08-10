"""
URL configuration for prueba1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from inicio import views as views_inicio
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path("juda/", views_inicio.nuevo, name="nuevo"),
    path("contacto/", views_registros.registrar, name="contacto"),
    path("formulario/", views_inicio.formulario, name="formulario"),
    path("ejemplo/", views_inicio.ejemplo, name="ejemplo"),
    path("registrar/", views_registros.registrar, name="Registrar"),
    path('', views_registros.registros, name='principal'),
    
    # Vista para consultas.html
    path("consultas/", views_registros.consultas, name="consultas"),
    
    # Vista para consultar_comentarios.html
    path("comentarios/", views_registros.consultar_comentarios, name="consultar_comentarios"),
    
    path('eliminarComentario/<int:id>/', views_registros.eliminarComentarioContacto, name='Eliminar'),
    
    # Rutas añadidas para la edición de comentarios
    path('editarComentario/<int:id>/', views_registros.editarComentarioContacto, name='Editar'),

    path('consultas1/', views_registros.consultar1, name='consultas1'),
    path('consultas2/', views_registros.consultar2, name='consultas2'),
    path('consultas3/', views_registros.consultar3, name='consultas3'),
    path('consultas4/', views_registros.consultar4, name='consultas4'),
    path('consultas5/', views_registros.consultar5, name='consultas5'),
    path('consultas6/', views_registros.consultar6, name='consultas6'),
    path('consultas7/', views_registros.consultar7, name='consultas7'),
    path('consultas8/', views_registros.consultar8, name='consultas8'),
    path('consultasSQL/', views_registros.consultasSQL, name='consultasSQL'),

    # Consultas con ORM
    path('consulta-orm-1/', views_registros.consulta_orm_1, name='consulta_orm_1'),
    path('consulta-orm-2/', views_registros.consulta_orm_2, name='consulta_orm_2'),
    path('consulta-orm-3/', views_registros.consulta_orm_3, name='consulta_orm_3'),
    path('consulta-orm-4/', views_registros.consulta_orm_4, name='consulta_orm_4'),
    path('consulta-orm-5/', views_registros.consulta_orm_5, name='consulta_orm_5'),

    # Consultas SQL directo
    path('consulta-sql-1/', views_registros.consulta_sql_1, name='consulta_sql_1'),
    path('consulta-sql-2/', views_registros.consulta_sql_2, name='consulta_sql_2'),
    path('consulta-sql-3/', views_registros.consulta_sql_3, name='consulta_sql_3'),
    path('consulta-sql-4/', views_registros.consulta_sql_4, name='consulta_sql_4'),
    path('consulta-sql-5/', views_registros.consulta_sql_5, name='consulta_sql_5'),

    # Rutas para la carga de archivos
    path('cargar-archivo/', views_registros.archivos, name='archivo'),
    path('cargar-archivo/', views_registros.archivos, name='Subir'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)