from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


# Create your views here.
class PostList(ListView):
    model = Post

# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts
#     )
class PostDetail(DetailView):
    model = Post

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post': post
#         }
#     )