"""
Определение форм
"""

from xml.dom.minidom import AttributeList
from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from .models import Comment, Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Форма аутентификации, которая использует BootstrapCSS."""
    username = forms.CharField(max_length=128,
                               min_length=3,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'
                                   })
                               )
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'
                                   })
                               )

class FeedBackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput({'class': 'form-control'}), label='Ваше имя', min_length=1, max_length=100)   # имя пользователя
    email = forms.EmailField(widget=forms.TextInput({'class': 'form-control'}), label='Ваш e-mail', min_length=7)               # email пользователя
    what_like = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 27, 'class': 'form-control'}), label='Что вам понравилось на нашем сайте?')
    what_imporved = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 27, 'class': 'form-control'}), label='Что можно улучшить?')
    what_add = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'cols': 27,'class': 'form-control'}), label='Что можно добавить?')
    recommend = forms.ChoiceField(widget=forms.RadioSelect, label='Вы порекомендуете нас своим друзьям и коллегам?', choices=[('1', 'Да'), ('2', 'Нет')], initial=1)
    satisfaction_level = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select'}), label='Как бы вы оценили общий уровень удовлетворенности работой нашего сайта?',
                                 choices=(('1', 'Крайне удовлетворён'),
                                          ('2', 'Удовлетворён'),
                                          ('3', 'Неудовлетворён'),
                                          ('4', 'Крайне неудовлетворён')), initial=1)
    latest_update = forms.BooleanField(widget=forms.CheckboxInput({'class': 'form-check-input'}), label='Нравится ли вам наше последнее обновление?', required=False)
    encountered_errors = forms.BooleanField(widget=forms.CheckboxInput({'class': 'form-check-input'}), label='Сталкивались ли вы с ошибками на сайте?', required=False)
    error_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 27, 'class': 'form-control'}), label='Попробуйте описать ошибку', required=False)

# email = forms.EmailField(widget=forms.TextInput(attrs={"class": "label"}), label='Ваш e-mail', min_length=7)

class CustomUserCreationForm(UserCreationForm):
    """Кастомная аутенфикация, которая использует BootstrapCSS"""
    username = forms.CharField(label='Имя пользователя', min_length=3, max_length=128, widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput({'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput({'class': 'form-control', 'placeholder': 'Пароль'}))
 
    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username = username)
        if new.count():
            raise ValidationError("Имя пользователя уже существует") 
        return username
 
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2
 
    def save(self, commit = True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            None,
            self.cleaned_data['password1']
        )
        return user

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment # Используемая модель
        fields = ('text',) # Требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text
        widgets = {'text': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваш комментарий здесь',
            'rows': '5',
            'cols': '50',
            })}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image')
        labels = {'title': 'Заголовок', 'description': 'Краткое содержание', 'content': 'Полное содержание', 'image': 'Картинка'}