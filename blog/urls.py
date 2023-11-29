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
]