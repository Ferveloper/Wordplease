from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from posts.models import Post

class LatestPostsView(View):

    def get(self, request):
        # Recuperar las últimas fotos de la base de datos
        posts = Post.objects.all().order_by('-modification_date').select_related('owner')

        # Creamos el contexto para pasarle las fotos a la plantilla
        context = {'latest_posts': posts[:5]}

        # Crear respuesta HTML con las fotos
        html = render(request, 'posts/latest.html', context)

        # Devolver la respuesta HTTP
        return HttpResponse(html)
