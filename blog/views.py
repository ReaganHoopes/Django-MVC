from time import strftime
import datetime

from django import template
from django.forms import forms
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Comments, Blog

from django.http import HttpResponse, HttpResponseRedirect


def plan(request):
    return render(request, 'blog/plan.html', {'now': strftime('%c')})

def about(request):
    return render(request, 'blog/about.html', {'now': strftime('%c')})

def techtipsWithCSS(request):
    return render(request, 'blog/techtips+css.html', {'now': strftime('%c')})

def techtipsWithoutCSS(request):
    return render(request, 'blog/techtips-css.html', {'now': strftime('%c')})




def blogArchive(request):
    entries = Blog.objects.order_by('-posted').all()
    commentsCount = []
    for i in range(len(entries)):
        commentsNum = len(Comments.objects.filter(blog=entries[i]))
        commentsCount.append(commentsNum)
    context = {'now': strftime('%c'), 'entries': entries, 'commentsCount':commentsCount}
    return render(request, 'blog/blogArchive.html', context)

def blogHome(request):
    entries = Blog.objects.order_by('-posted')[:3]
    commentsCount = []
    for i in range(len(entries)):
        commentsNum = len(Comments.objects.filter(blog=entries[i]))
        commentsCount.append(commentsNum)
    context = {'now': strftime('%c'), 'entries': entries,'commentsCount':commentsCount}
    return render(request, 'blog/blogHome.html', context)

def blogEntry(request, id):
    entry = Blog.objects.get(id=id)
    comments = Comments.objects.filter(blog=entry).order_by('-posted')
    commentsCount = len(comments)
    context = {'now': strftime('%c'), 'entry': entry, 'comments':comments, 'commentsCount':commentsCount}
    return render(request, 'blog/blogEntry.html', context)

def comment(request, id):
    entry = get_object_or_404(Blog, pk=id)
    try:
        comment = Comments(blog=entry, commenter=request.POST.get('commenter'),email =request.POST.get('email'), content = request.POST.get('comment'))

    except(KeyError, Comments.DoesNotExist):
        return render(request, {'error_message': "You didn't select a choice."})
    comment.save()
    return HttpResponseRedirect(reverse('blog:entry', args=(id,)))
