from django import forms
from django.forms import ModelForm
from .models import *


class SwahiliCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']


class SwahiliSubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['title','cat']


class SwahiliContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title','main_cat','category','content','date_created','author']

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'main_cat':forms.Select(attrs={'class': 'form-control'}),
            'category':forms.Select(attrs={'class': 'form-control'}),
            'content':forms.Textarea(attrs={'class': 'form-control'}),
            'date_created':forms.TextInput(attrs={'class': 'form-control'}),
            'author':forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'author', 'type':'hidden'}),
            # 'author':forms.Select(attrs={'class': 'form-control'}),
        }

class addCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
