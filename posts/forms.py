import datetime

from django import forms
from django.forms import ModelForm

from posts.models import Category, Post


class NewPostForm(forms.Form):

    # class Meta:
    #     model = Post
    #     fields = ['title', 'url', 'introduction', 'body', 'publication_date', 'categories']

    title = forms.CharField(label='Título')
    url = forms.URLField(label='URL de imagen')
    intro = forms.CharField(label='Introducción', widget=forms.Textarea())
    body = forms.CharField(label='Cuerpo del artículo', widget=forms.Textarea())
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all().order_by('name'))
    pub_date = forms.DateTimeField(label='Fecha de publicación (DD/MM/YYYY HH:MM)', widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M'), input_formats=('%d/%m/%Y %H:%M', ))
