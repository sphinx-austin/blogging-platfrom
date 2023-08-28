from django.shortcuts import render
from . models import Post
from django.views.generic import ListView, DetailView, CreateView, DeleteView


# view here

class HomeView(ListView):
    model = Post
    context_object_name = ''
    template_name = 'posts/home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'posts/article_details.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'posts/add_post.html'
    fields = '__all__'
    # fields = ('title', 'body')
