from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.feed, name = "feed"),
    path('<int:blog_id>/', views.article, name="article"),
    path('writer/<int:blogger_id>/', views.writer, name="writer"),
    path('add_blog/', views.AddBlog.as_view(), name='add_blog'),
    path('add_blogger/', views.AddBlogger.as_view(), name='add_blogger'),
    path('add_student/', views.AddStudent.as_view(), name='add_student'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('gallery/', views.gallery, name='gallery'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('imagedelete/<int:id>', views.imagedelete),

]