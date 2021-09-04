from django.db import models

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse

from madapalace.utils import unique_slug_generator
from django.db.models.signals import pre_save


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    cat = models.ForeignKey(Category,blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Content(models.Model):
    #TODO: the id for arrangement
    title = models.CharField(max_length=100)
    main_cat = models.ForeignKey(Category,blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(SubCategory,blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(null=True, blank=True)
    date_created = models.DateField()
    # date_modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    #date_published = models.DateTimeField(default=timezone.now, null=True, blank=True)
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='swahili_content')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('swahili_detail', args=[str(self.slug)])


class Comment(models.Model):
    post = models.ForeignKey(Content, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title} - {self.name}'



def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Category)
pre_save.connect(slug_generator, sender=SubCategory)
pre_save.connect(slug_generator, sender=Content)
