from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name='login'),
    path('logout/',views.logout_view, name= 'logout'),
    path('registro/',views.registro_view,name='registro'),
    path('registro/error/',views.error_view,name='error'),
    path('listar/',views.listar_view, name='listar'),
    path('listar/modificar/<str:pk>/',views.modificar_view, name='modificar'),
    path('listar/modificar/<str:pk>/eliminar/',views.eliminar_view, name='eliminar'),
    path('export_xls/',views.export_csv, name ='export_xls'),
]
