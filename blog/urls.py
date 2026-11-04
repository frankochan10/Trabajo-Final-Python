from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    AcercaDeMiView,
)

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='inicio'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detalle'),
    path('post/nuevo/', PostCreateView.as_view(), name='post_crear'),
    path('post/<int:pk>/editar/', PostUpdateView.as_view(), name='post_editar'),
    path('post/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_eliminar'),
    path('acerca-de-mi/', AcercaDeMiView.as_view(), name='acerca_de_mi'),
]