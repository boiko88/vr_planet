from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_list = Blog.objects.all()
        paginator = Paginator(blog_list, self.paginate_by)
        page = self.request.GET.get('page')
        blogs = paginator.get_page(page)
        context['blogs'] = blogs
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
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        blog_list = Blog.objects.filter(blog_name__contains=query)
        return blog_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
        context['blogs'] = blogs
        return context
