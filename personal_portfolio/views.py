from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post

def homepage(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)  # Show 2 item per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)