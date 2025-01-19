from django.db import models
from cloudinary.models import CloudinaryField

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)  # Imagen usando Cloudinary
    link = models.URLField(blank=True, null=True)  # Enlace opcional
    published_at = models.DateTimeField(auto_now_add=True)  # Fecha de publicación automática

    def __str__(self):
        return self.title
