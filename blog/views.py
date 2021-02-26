from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Unknown',
        'title': 'First Blog',
        'content': 'First post upload',
        'date_posted': '20th Feb 2021'
    },
    {
        'author': 'Manager L',
        'title': 'Second Blog',
        'content': 'Can blog + vlog',
        'date_posted': '24th Feb 2021'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
