from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView,View,TemplateView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog,Comment,Likes,Dislikes
import uuid
# Create your views here.

def blog_list(request):
    return HttpResponse('Welcome to Blog List Page')


#Create Blog

class CreateBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title','blog_content','blog_image')

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('home'))
    

#Blog Liat
class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'
    queryset = Blog.objects.order_by('-publish_date')
    #paginate_by = 10


#Blog Detail
def blog_detail(request,slug):
    blog = Blog.objects.get(slug=slug)
    #comment = Comment.objects.filter(blog=blog)
    #context = {'blog':blog,'comment':comment}
    return render(request,'App_Blog/blog_detail.html',context={'blog':blog})