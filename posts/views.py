from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .forms import PostForm
# Create your views here.

def posts_list(request):
    # posts = Post.objects.filter(status="published")
    # page_number = request.GET.get("page", 1)
    # per_page = request.GET.get("per_page", 50)
    # paginator = Paginator(posts, per_page)

    # page_obj = paginator.page(page_number)

    return render(request, "posts/list.html")
# , {"page_obj": page_obj}


def post_details(request, post_id):
    form = None
    post = get_object_or_404(Post, id=post_id, status="published")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

    if request.user == post.author:
        form = PostForm(instance=post)

    # post = Post.objects.get(id=post_id, status="published")
    return render(request, "posts/details.html", {"post": post, "form": form})


def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if request.user.is_superuser:
                post.status = "published"
            post.save()
            return redirect("posts:list")
    return render(request, "posts/create.html", {"form": form})
