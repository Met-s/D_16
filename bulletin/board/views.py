
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = '-post_date'
    template_name = 'board/post_list.html'
    context_object_name = 'posts'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'add_post'
    form_class = PostForm
    model = Post
    template_name = 'board/post_create.html'
    context_object_name = 'post_create'

    def post(self, *args):
        return reverse('post_create')


class PostDetail(DetailView):
    model = Post
    template_name = 'board/post.html'
    context_object_name = 'post'

