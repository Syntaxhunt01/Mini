from django.db import models

class UploadedImage(models.Model):
    original_image = models.ImageField(upload_to='originals/')
    filterered_image = models.ImageField(upload_to='filtered/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
