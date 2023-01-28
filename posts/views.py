from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Post

POST_LIST_TEMPLATE = '''
        <h1>{title}</h1><br>
        <h3>tags: {tags}</h3><br>
        <div><i>{content}</i><div>
        <br>\n
    '''

def format_post(post):
    return POST_LIST_TEMPLATE.format(
        title=post.title,
        tags=post.tags,
        content=post.content,
    )

def index(request):
    context = {
        'all_posts': Post.objects.order_by('-pub_date')
    }

    return render(request, 'posts/index.html', context)

def show(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        output = format_post(post)
    except Post.DoesNotExist:
        raise Http404("Esse post não existe.")
    return HttpResponse(output)
