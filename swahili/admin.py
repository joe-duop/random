from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.SwahiliCategory)
admin.site.register(models.SwahiliSubCategory)
admin.site.register(models.SwahiliContent)
