from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post

# Create your views here.

def post_list(request):
    qs = Post.objects.none()
    
    q = request.GET.get('q', '')
    
    # 검색어 띄어쓰기에 따라 OR로 검색 방법 1
    if q=='':
        qs = Post.objects.all()

    else:
        q_split = q.strip().split(" ")
        for word in q_split:
            t_qs = Post.objects.filter(title__contains=word)
            qs = qs | t_qs

    return render(request, 'blog/post_list.html', {
        'post_list' : qs,
        'q' : q, 
    })


def post_detail(request, id):

    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404

    post = get_object_or_404(Post, id=id)

    return render(request, 'blog/post_detail.html', {
        'post':post,
    })