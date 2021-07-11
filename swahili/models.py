from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from madapalace.utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.
class SwahiliCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title


class SwahiliSubCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    cat = models.ForeignKey(SwahiliCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SwahiliContent(models.Model):
    #TODO: the id for arrangement
    title = models.CharField(max_length=100)
    main_cat = models.ForeignKey(SwahiliCategory, on_delete=models.CASCADE)
    category = models.ForeignKey(SwahiliSubCategory, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    date_created = models.DateField()
    #date updated
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=SwahiliCategory)
pre_save.connect(slug_generator, sender=SwahiliSubCategory)
pre_save.connect(slug_generator, sender=SwahiliContent)
