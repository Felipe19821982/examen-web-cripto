from django.urls import path
from . import views
from .views import logout_view, exit
from .views import mensajes, marcar_respondido, contacto

urlpatterns = [
    path('index/', views.index, name='index'),
    path('listadoSQL/', views.listadoSQL, name='listadoSQL'),
    path('criptoactivos/', views.criptoactivos, name='criptoactivos'),
    path('comprar/', views.comprar, name='comprar'),
    path('vender/', views.vender, name='vender'),
    path('registro/', views.registro_view, name='registro'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('logout/', exit, name='exit'),
    path('mis_compras/', views.mis_compras, name='mis_compras'),
    path('mensajes/', views.mensajes, name='mensajes'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/eliminar/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuarios/editar/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/restablecer_contrasena/<int:user_id>/', views.restablecer_contrasena, name='restablecer_contrasena'),
    path('mensajes/', mensajes, name='mensajes'),
    path('mensajes/respondido/<int:mensaje_id>/', marcar_respondido, name='marcar_respondido'),
    path('contacto/', contacto, name='contacto'),
]