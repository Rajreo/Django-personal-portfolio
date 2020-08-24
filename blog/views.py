from django.shortcuts import render,get_object_or_404
from .models import Blog_project
# Create your views here.
def all_blogs(request):
    blogs=Blog_project.objects.order_by('-Date')
    return render(request,'blog/blog.html',{'blogs':blogs})

def detail(request,blog_id):
    blogs=get_object_or_404(Blog_project,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blogs})