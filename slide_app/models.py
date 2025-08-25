from django.db import models

# Create your models here.
class Slide(models.Model):
    title = models.CharField(max_length=50, verbose_name="otsikko (pakollinen)")
    image = models.ImageField(upload_to='slide_app', verbose_name="kuva",editable=True)

    def __str__(self):
        return self.title
