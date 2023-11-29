from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, Blogger
from django.db.models import Count
from django.views import View
from django.utils import timezone
from .forms import studentForm

# Create your views here.
def feed(request):
    blogs = Blog.objects.select_related('blogger').order_by("-pub_date")
    ranks = Blogger.objects.annotate(blog_count = Count('blog')).order_by('-blog_count')[:5]
    blog_data = []
    for blog in blogs:
        blog_data.append({
            "blog_id":blog.id,
            "title" : blog.title,
            "body":blog.body,
            "pub_date":blog.pub_date,
            "blogger": blog.blogger.name,
            "blogger_id":blog.blogger.id,
        })
    context = {
        "title": "feed",
        "blog_data":blog_data,
        "ranks": ranks,
    }
    return render(request, "blog/index.html",context)

def article(request, blog_id):
    blog = Blog.objects.get(pk = blog_id)

    context = {
        "blog":blog,
        "title": "blog",
    }
    return render(request, "blog/blog.html", context)


def writer(request, blogger_id):
    writer = Blogger.objects.get(pk = blogger_id)
    blogs = writer.blog_set.all().order_by("-pub_date")
    title = "writer"
    context = {
        "writer":writer,
        "title": title,
        "blogs":blogs,
    }
    return render(request, 'blog/writer.html', context)

class AddBlog(View):

    def get(self, request):

        bloggers = Blogger.objects.all()
        body = request.session.get('body', False)

        if (body) : del(request.session['body'])
        
        context = {
            "bloggers": bloggers,
            "title": AddBlog,
            "message": body,
        }
        
        return render(request, 'blog/add_blog.html', context)
    
    def post(self, request):

        body = request.POST.get("body")
        title = request.POST.get("title")
        blogger = request.POST.get("blogger")

        b = Blogger.objects.get(name = blogger)
        b.blog_set.create(body = body, title = title, pub_date = timezone.now())
        request.session['message'] = body

        return redirect(request.path)
    
class AddBlogger(View):

    def get(self, request):
        bio = request.session.get('bio', False)

        if (bio) : del(request.session['message'])
        
        context = {
            "message": bio,
        }
        
        return render(request, 'blog/add_blogger.html', context)
    
    def post(self, request):

        bio = request.POST.get("bio")
        name = request.POST.get("name")
        username = request.POST.get("username")
        Blogger(bio = bio, name = name, username = username).save()
        request.session['message'] = bio

        return redirect(request.path)
    
class AddStudent(View):

    def get(self, request):
        form = studentForm()
        context = {
            "form" : form
        }
        return render(request, 'blog/student.html', context=context)
    
    def post(self, request):

        form = studentForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            course = form.cleaned_data['course']
            context = {
                'name' : name,
                'age' : age,
                'course' : course
            }
            return HttpResponse(context)
        
        return HttpResponse("not valid")