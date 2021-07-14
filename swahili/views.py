from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.
def homeView(request):
    return render(request, 'home.html')


#main category
def swahiliCategoryView(request):
    """lists all the categories created"""
    sw_main = SwahiliCategory.objects.all()
    context = {'sw_main':sw_main}
    return render(request, 'category/swahiliCategoryView.html', context)

def swahiliCategoryCreateView(request):
    if request.method == 'POST':
        form = SwahiliCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        context = {'form':SwahiliCategoryForm()}
        return render(request, "category/swahiliCategoryCreateView.html", context)

def swahiliCategoryDetailView(request, the_slug):
    """shows the details of a specific category - the sub-categories"""
    sw_main_det = SwahiliCategory.objects.get(slug=the_slug)
    context = {'sw_main_det':sw_main_det}
    return render(request, 'category/swahiliCategoryDetailView.html', context)


# sub-category
def swahiliSubCategoryView(request):
    """lists all the swahili-sub-categories created"""
    sw_sub = SwahiliSubCategory.objects.all()
    context = {'sw_sub':sw_sub}
    return render(request, 'sub_category/swahiliSubCategoryView.html', context)

def swahiliSubCategoryCreateView(request):
    if request.method == 'POST':
        form = SwahiliSubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sub_category')
    else:
        context = {'form':SwahiliSubCategoryForm()}
        return render(request, "sub_category/swahiliSubCategoryCreateView.html", context)

def swahiliSubCategoryDetailView(request, slug):
    """shows the details of a specific swahili-sub-category - the contents"""
    sw_sub_det = SwahiliSubCategory.objects.get(slug=slug)
    context = {'sw_sub_det':sw_sub_det}
    return render(request, 'sub_category/swahiliSubCategoryDetailView.html', context)


# content
def swahiliView(request):
    """lists all the topics created"""
    swahili = SwahiliContent.objects.all()
    context = {'swahili':swahili}
    return render(request, 'topic/swahiliView.html', context)


def swahiliCreateView(request):
    if request.method == 'POST':
        form = SwahiliContentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('swahili')
    else:
        context = {'form':SwahiliContentForm()}
        return render(request, "topic/swahiliCreateView.html", context)


def swahiliUpdateView(request, slug_text):
    """allows a user to edit/update content"""
    edit_content = get_object_or_404(SwahiliContent, slug=slug_text)
    if request.method == 'POST':
        content_form = SwahiliContentForm(request.POST, instance=edit_content)
        if content_form.is_valid():
            content_form.save()
            return redirect('swahili')
    else:
        content_form = SwahiliContentForm(instance=edit_content)
        context = {'edit_content':edit_content, 'content_form':content_form}
        return render(request, 'topic/swahiliUpdateView.html', context)


def swahiliDetailView(request, slug_text):
    """shows the details of a specific topic - the contents"""
    swahili_det = get_object_or_404(SwahiliContent, slug=slug_text)
    context = {'swahili_det':swahili_det}
    return render(request, 'topic/swahiliDetailView.html', context)
