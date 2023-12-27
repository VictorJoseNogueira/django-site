from django.contrib.auth.models import User
from django.db import models
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=65)



class Recipe(models.Model):
    tittle = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
        )
    
    Author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
        )

# EDITED
# TITTLE DESCRIPTION SLUG
# PREPARATION_TIME PREPARATION_TIME_UNIT
# servings servings_units
# preparation_steps
# preparation_steps_is_html
# created_at update_at
# is_published
# cover
# category (relação)
# Author( relação)
 