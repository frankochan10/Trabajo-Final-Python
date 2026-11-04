from django.urls import path
from .views import registro, CustomLoginView, CustomLogoutView, editar_perfil

app_name = 'cuentas'

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('perfil/', editar_perfil, name='perfil'),
]