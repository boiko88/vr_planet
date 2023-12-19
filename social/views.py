from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, ListView

from .serializers import UserSerializer
from . models import Blog
from . forms import LoginForm


class MyView(View):
    def get(self, request):
        return render(request, self.template_name)


class HomeView(MyView):
    template_name = 'home.html'


class EquipmentView(MyView):
    template_name = 'equipment.html'


class GamesView(MyView):
    template_name = 'games.html'


class HeadsetsView(MyView):
    template_name = 'headsets.html'


class ForumView(MyView):
    template_name = 'forum.html'


class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login1.html', {'form': form})


class BlogSearchView(ListView):
    model = Blog
    template_name = 'blog_search.html'
    context_object_name = 'blogs'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            return Blog.objects.filter(blog_name__contains=query)
        return Blog.objects.all()
