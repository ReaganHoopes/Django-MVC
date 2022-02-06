from django.http import HttpRequest
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('home/', views.blogHome, name='home'),
    path('archive/', views.blogArchive, name='archive'),
    path('home/<int:id>/', views.blogEntry, name='entry'),
    path('archive/<int:id>/', views.blogEntry, name='entry'),
    path('index/<int:id>/', views.blogEntry, name='entry'),
    path('index/', views.blogHome, name='home'),
    path('<int:id>/', views.blogEntry, name ='entry'),
    path('about/', views.about, name='about'),
    path('plan/', views.plan, name = 'plan'),
    path('techtips+css/', views.techtipsWithCSS, name = 'techtips+css'),
    path('techtips-css/', views.techtipsWithoutCSS, name = 'techtips-css'),
    path('<int:id>/comment/', views.comment, name="comment")
]