from django import forms
from django.forms import ModelForm
from .models import *


class SwahiliCategoryForm(forms.ModelForm):
    class Meta:
        model = SwahiliCategory
        fields = ['title']


class SwahiliSubCategoryForm(forms.ModelForm):
    class Meta:
        model = SwahiliSubCategory
        fields = ['title','cat']


class SwahiliContentForm(forms.ModelForm):
    class Meta:
        model = SwahiliContent
        fields = ['title','main_cat','category','content','date_created','author']
