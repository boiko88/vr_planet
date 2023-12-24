from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from . serializers import UserSerializer
from . models import Blog, Game
from . forms import LoginForm


class MyView(View):
    def get(self, request):
        return render(request, self.template_name)


class HomeView(MyView):
    template_name = 'home.html'


class EquipmentView(MyView):
    template_name = 'equipment.html'


class GamesView(TemplateView):
    template_name = 'games.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game_list = Game.objects.all()
        paginator = Paginator(game_list, self.paginate_by)
        page = self.request.GET.get('page')
        games = paginator.get_page(page)
        context['games'] = games
        return context


class HeadsetsView(MyView):
    template_name = 'headsets.html'


class ForumView(MyView):
    template_name = 'forum.html'

# Blog CRUD


class BlogMixin(object):
    model = Blog
    success_url = reverse_lazy('blog')
    fields = ['blog_name', 'blog_description', 'blog_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogCreate(BlogMixin, CreateView):
    template_name = 'blog_create.html'
    success_url = reverse_lazy('blog')


class BlogUpdate(UpdateView):
    model = Blog
    fields = ['blog_name', 'blog_description', 'blog_image']
    template_name = 'blog_update.html'
    success_url = reverse_lazy('blog')


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog')

    def get_object(self, queryset=None):
        blog_id = self.kwargs.get('blog_id')
        return Blog.objects.get(id=blog_id)


class BlogView(BlogMixin, TemplateView):
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
