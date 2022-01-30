from django.db import models
from django.db.models.fields import SlugField
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products' , null=True , blank=True)
    slug = SlugField(null=True , blank=True)
    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            return super(Product , self).save(*args, **kwargs)


