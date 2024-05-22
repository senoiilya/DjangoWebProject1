"""
Definition of views.
"""

from code import interact
from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpRequest
from .forms import BlogForm, FeedBackForm, CustomUserCreationForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Blog, Comment

def home(request):
    """Отображает главную страницу."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/main.html',
        {
            'title':'Домашняя страница', # Эти константы не используются
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Отображает страницу 'Контакты'."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'year':datetime.now().year, # Эта константа не используется
        }
    )

def about(request):
    """Отображает страницу 'О нас'."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Страница описания твоего приложения.',  # Эта константа не используется
            'year':datetime.now().year,  # Эта константа не используется
        }
    )

def links(request):
    """Отображает страницу 'Полезные ресурсы'."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title': 'Полезные ресурсы',
            'year':datetime.now().year, # Эта константа не используется
        }
    )

def feedback(request):
    """Отображает страницу с отзывом"""
    assert isinstance(request, HttpRequest)
    data = None
    
    recomend_statements = {'1': 'Да', '2': 'Нет'}
    satisfaction_statements = {'1': 'Крайне удовлетворён', '2': 'Удовлетворён', 
                '3': 'Неудовлетворён', '4': 'Крайне неудовлетворён'}
    
    if request.method == 'POST':
        feedbackform = FeedBackForm(request.POST)
        if feedbackform.is_valid():
            data = dict()
            data['name'] = feedbackform.cleaned_data['name']
            data['email'] = feedbackform.cleaned_data['email']
            data['what_like'] = feedbackform.cleaned_data['what_like']
            data['what_imporved'] = feedbackform.cleaned_data['what_imporved']
            data['what_add'] = feedbackform.cleaned_data['what_add']
            data['recommend'] = recomend_statements[feedbackform.cleaned_data['recommend']]
            data['satisfaction_level'] = satisfaction_statements[feedbackform.cleaned_data['satisfaction_level']]
            if (feedbackform.cleaned_data['latest_update']):
                data['latest_update'] = 'Да'
            else:
                data['latest_update'] = 'Нет'
            if (feedbackform.cleaned_data['encountered_errors']):
                data['encountered_errors'] = 'Да'
            else:
                data['encountered_errors'] = 'Нет'
            data['error_description'] = feedbackform.cleaned_data['error_description']
            feedbackform = None
    else:
        feedbackform = FeedBackForm()
    return render(
        request,
        'app/pool.html',
        {
            'form':feedbackform,
            'data':data
        }
    )

def registration(request):
    """Отображает страницу регистрации"""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        regform = CustomUserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()

            reg_f.save()
        return redirect('home')
    else:
        regform = CustomUserCreationForm()
    return render(
        request, 
        'app/registration.html', 
        {
            'regform': regform,
            'title': 'Регистрация пользователя',
        })

def blog(request):
    """Отображает страницу со статьями блога"""
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели
    return render(
        request,
        'app/blog.html',
        {
            'title':'Бильярд: история появления, разновидности и правила игры',
            'posts': posts, # передача списка статей в шаблон веб-страницы
        }
    )

def blogpost(request, parametr):
    """Отображает страницу конкретной статьи блога"""
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_f = comment_form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()
        return redirect('blogpost', parametr=post_1.id)
    else:
        comment_form = CommentForm()
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1,
            'comments': comments,
            'form': comment_form, 
        }
    )

def newpost(request):
    """Отображает страницу создания статьи"""
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()
        return redirect('blog')
    else:
        blogform = BlogForm()
    return render(
        request,
        'app/newpost.html',
        {
            'form': blogform,
            'title': 'Добавить статью блога',
        }
    )

def videopost(request):
    """Отображает страницу с видео"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видео',
        }
    )