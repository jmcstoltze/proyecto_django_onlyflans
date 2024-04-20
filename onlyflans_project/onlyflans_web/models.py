from django.db import models
from uuid import uuid4

# Create your models here.

class Flan(models.Model):

    # Se genera automáticamente y es único
    flan_uuid = models.UUIDField(default=uuid4, editable=False, unique=True) 
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    # Debe ingresarse manualmente pero puede crearse un método para su generación automática
    slug = models.SlugField(unique=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class ContactForm(models.Model):

    contact_form_uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_name
