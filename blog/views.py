from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

posts = [
    {
        "title": "Learning Django",
        "author": "Archana Gujar",
        "content": "I am happy to learn Django.",
        "date_posted": "March 19, 2023"
    },

    {
        "title": "Learning Flask",
        "author": "Archana Gujar",
        "content": "I like flask. It is easy to use and very light weight.",
        "date_posted": "March 18, 2023"
    }
]

def home(request):
    content = {"posts": posts, 'title': 'Home'}
    return render(request, 'blog/home.html', content)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})