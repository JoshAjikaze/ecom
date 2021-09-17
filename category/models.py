from django.db import models

# Create your models here.
class Category(models.Model):
    category_name =  models.CharField(max_length=50)
    slug =  models.CharField(max_length=50, unique=True)
    description =  models.CharField(max_length=50)
    cat_image = models.ImageField(upload_to='photos/categories')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.category_name