from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):   # This function takes a request and returns a function render that put templates together
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # This queryset is to sort
    return render(request, 'wardrobe/post_list.html', {'posts': posts})


def post_detail(request, pk):   # This function takes a request as well as the primary key of the requested post and returns a function render that put templates together
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'wardrobe/post_detail.html', {'post': post})


def post_new(request):   # this function deals with two situations: if access the page for the first time and we want a blank page; or if coming back to the view with all data typed
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'wardrobe/post_edit.html', {'form': form})


def post_edit(request, pk):  # This function takes a request and the associated primary key and then gets the post model we want to edit with
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'wardrobe/post_edit.html', {'form': form})
# Create your views here.
