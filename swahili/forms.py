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

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'main_cat':forms.Select(attrs={'class': 'form-control'}),
            'category':forms.Select(attrs={'class': 'form-control'}),
            'content':forms.Textarea(attrs={'class': 'form-control'}),
            'date_created':forms.TextInput(attrs={'class': 'form-control'}),
            'author':forms.Select(attrs={'class': 'form-control'}),
        }
