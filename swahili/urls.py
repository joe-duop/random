from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),
    #main_category
    path('category', views.swahiliCategoryView, name="category"),
    path('category/<slug:the_slug>/', views.swahiliCategoryDetailView, name='category_detail'),
    #sub_category
    path('sub_cat', views.swahiliSubCategoryView, name="sub_category"),
    path('sub_cat/<slug:slug>/', views.swahiliSubCategoryDetailView, name='sub_category_detail'),
    #content
    path('topic', views.swahiliView, name="swahili"),
    path('topic/<slug:slug_text>', views.swahiliDetailView, name='swahili_detail'),
]
