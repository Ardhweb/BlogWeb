from turtle import title
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,\
 PageNotAnInteger
from django.db.models import Q


def home(request):
    # post = Post.published.filter(Q(title='Html test post') | Q (title='pc')).values()
    post = Post.published.order_by('-created_at').all()[:3]
    return render(request, 'home.html', {'post':post})







def post_listing(request):
    post_list = Post.published.all()  #Here published is Custom Model Manager Look to model file.
    paginator = Paginator(post_list, 3) #show only 3 post each pages
    page_obj  = request.GET.get('page')
    posts_obj = paginator.get_page(page_obj)
    #return render(request, 'blog/post-listing.html', {'post_list':post_list})
    return render(request, 'blog/post-listing.html', {'posts_obj': posts_obj,'page_obj':page_obj})



def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug=post, status='published',
    publish__year=year,
    publish__month=month,
    publish__day=day)
    return render(request, 'blog/post-detail.html', {'post':post})






def search_post(request):
    if request.method == "POST":
        searched = request.POST['searched']
        search_results = Post.published.filter(title__contains = searched)
        return render(request, "search-page.html",{"searched":searched,"search_results":search_results} )
    else:
        return render(request, "search-page.html",{} )

