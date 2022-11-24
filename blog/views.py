from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import   Post , Post_Pic
# Create your views here.


def index(request):
    context={}
    post_pic_list=[]
    BlogList= Post.objects.all().order_by("-id")
    page = request.GET.get('page', 1)
    paginator = Paginator(BlogList, 2)
    
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
        
    for i in post_list.object_list:
      post_pic_list.append(Post_Pic.objects.filter(post=i.id)[0])

    context['posts'] = post_list
    context['Post_img'] = post_pic_list
    return render(request,'blog.html', context)


def Post_Specific(request , id = id):
        context = {}
        Specific_post = get_object_or_404(Post,id=id)
        recentPOsted= Post.objects.all().order_by('-id')[:5]
        post_pic_list = Post_Pic.objects.filter(post=Specific_post.id)[0]
        context['post_pic'] = post_pic_list    
        context['post_details'] = Specific_post
        context['recentPOsted'] = recentPOsted
        return render(request,'contentofblog.html',context)
    


