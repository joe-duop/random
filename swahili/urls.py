from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),

    # path('cat', views.kiswahiliCategoryView, name="cat"),
    # path('cat/<slug:the_slug>/', views.kiswahiliCategoryDetailView, name='cat_detail'),
    #
    # path('category', views.categoryView, name="category"),
    # path('category/<slug:slug>/', views.categoryDetailView, name='category_detail'),
    #
    # path('sarufi', views.sarufiView, name="sarufi"),
    # path('sarufi/<slug:slug_text>', views.sarufiDetail, name='sarufi_detail'),
]
