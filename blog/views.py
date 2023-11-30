from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Blogger
from django.db.models import Count
from django.views import View
from django.utils import timezone
from .forms import studentForm, LoginForm, SignupForm, editForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login

# Create your views here.

def delete_blog(request, blog_id):
    blog= get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Blog deleted successfully.')
        return redirect('blog:feed')

    context = {
        'blog': blog,
        'title': 'Delete Blog',
    }
    return render(request, 'blog/delete_blog.html', context)

def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        form = editForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog edited successfully.')
            return redirect('blog:feed')
    else:
        form = editForm(instance=blog)

    context = {
        'form': form,
        'blog': blog,
        'title': 'Edit Blog',
    }
    return render(request, 'blog/edit_blog.html', context)

def user_logout(request):
    logout(request)
    return redirect('blog:login')

@login_required(login_url='blog:login')
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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username',)
        password = request.POST.get('password',)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('blog:feed')  
        return render(request, 'blog/index.html', {'error': 'Invalid login credentials'})
    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'blog/login.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
                return redirect('blog:signup')

            User.objects.create_user(username=username, password=password)
            
            return redirect('blog:login')
        else:
            return redirect(request.path)
    form = SignupForm()
    return render(request, 'blog/signup.html',{'form':form})

    

