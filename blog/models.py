from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    subtitulo = models.CharField(max_length=250, verbose_name="Subtítulo", blank=True)
    contenido = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True, verbose_name="Imagen de portada")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name="Autor")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return f"{self.titulo} - por {self.autor.username}"