from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, DetailView,
                                  UpdateView, DeleteView)
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = '-post_date'
    template_name = 'board/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostDetail(DetailView):
    model = Post
    template_name = 'board/post.html'
    context_object_name = 'post'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'add_post'
    form_class = PostForm
    model = Post
    template_name = 'board/post_create.html'
    context_object_name = 'post_create'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'board.add_post'
    form_class = PostForm
    model = Post
    template_name = 'board/post_create.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'board/add_post'
    model = Post
    template_name = 'board/post_delete.html'
    success_url = reverse_lazy('post_list')





