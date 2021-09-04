from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import *

from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def homeView(request):
    return render(request, 'home.html')


def signUpUser(request):
    if request.method == 'GET':
        return render(request, 'signUpView.html', {'form':UserCreationForm()})
    else:
        """if the request.method is post"""
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('login')
            except IntegrityError:
                return render(request, 'signUpView.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'signUpView.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})



#main category
def swahiliCategoryView(request):
    """lists all the categories created"""
    sw_main = Category.objects.all()
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
    sw_main_det = Category.objects.get(slug=the_slug)
    context = {'sw_main_det':sw_main_det}
    return render(request, 'category/swahiliCategoryDetailView.html', context)


# sub-category
def swahiliSubCategoryView(request):
    """lists all the swahili-sub-categories created"""
    sw_sub = SubCategory.objects.all()
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


def swahiliSubCategoryUpdateView(request, slug):
    """allows a user to edit/update sub-category"""
    edit_sub = get_object_or_404(SubCategory, slug=slug)
    if request.method == 'POST':
        sub_form = SwahiliSubCategoryForm(request.POST, instance=edit_sub)
        if sub_form.is_valid():
            sub_form.save()
            return redirect('swahili')
    else:
        sub_form = SwahiliSubCategoryForm(instance=edit_sub)
        context = {'edit_sub':edit_sub, 'sub_form':sub_form}
        return render(request, 'sub_category/swahiliSubCategoryUpdateView.html', context)



def swahiliSubCategoryDetailView(request, slug):
    """shows the details of a specific swahili-sub-category - the contents"""
    sw_sub_det = SubCategory.objects.get(slug=slug)
    context = {'sw_sub_det':sw_sub_det}
    return render(request, 'sub_category/swahiliSubCategoryDetailView.html', context)


# content
def swahiliView(request):
    """lists all the topics created"""
    swahili = Content.objects.all()
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
    edit_content = get_object_or_404(Content, slug=slug_text)
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
    swahili_det = get_object_or_404(Content, slug=slug_text)
    total_likes = swahili_det.total_likes()

    liked = False
    if swahili_det.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == 'POST':
        form = addCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('swahili')
    else:
        context = {'form':addCommentForm()}

    context = {'swahili_det':swahili_det, 'total_likes':total_likes, "liked":liked, 'form':addCommentForm()}
    return render(request, 'topic/swahiliDetailView.html', context)

# def swahiliAddComment(request):
#     if request.method == 'POST':
#         form = addCommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('swahili')
#     else:
#         context = {'form':addCommentForm()}
#         return render(request, "topic/swahiliDetailView.html", context)


def likeView(request, pk):
    like_c = get_object_or_404(Content, id=request.POST.get('post_id'))
    liked = False
    if like_c.likes.filter(id=request.user.id).exists():
        like_c.likes.remove(request.user)
        liked = False
    else:
        like_c.likes.add(request.user)
        liked = True
    return redirect('swahili')
