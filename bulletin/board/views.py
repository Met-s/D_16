
from django.shortcuts import render, redirect
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
    paginate_by = 5


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'add_post'
    form_class = PostForm
    model = Post
    template_name = 'board/post_create.html'
    context_object_name = 'post_create'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# def add_post(request):
#     if form_class.is_valid():
#             post_item = form_class.save(commit=False)
#             post_item.save()
#             return redirect('post_list')
#     else:
#         form = PostForm()
#     return render(request, 'reply/post_form.html',
#                   {'form': form})

    # def post(self, *args):
    #     return reverse('post')


class PostDetail(DetailView):
    model = Post
    template_name = 'board/post.html'
    context_object_name = 'post'

