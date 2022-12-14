from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from . import forms

def Index(request):
    context = {
        'num_books' : models.Book.objects.all().count(),
        'num_authors': models.Author.objects.all().count(),
        'num_instances_available': models.BookInstance.objects.all().count(),
        'num_instances': models.BookInstance.objects.filter(status__exact='a').count()
    }

    return render(request,'app/index.html' , context)

@login_required
def Book_list(request):
    context = {
        'book_list' : models.Book.objects.all()
    }

    return render(request,'app/Book_list.html' , context)

def Book_detail(request , pk):
    context = {
        'book' : models.Book.objects.filter(pk=pk)[0]
    }

    return render(request,'app/book_detail.html' , context)


def test(request):
    if request.method == "POST":
        form = forms.TestForm(request.POST)
    else:
        form = forms.TestForm()

    return render(request, 'app/form.html', {'form': form})


def Author(request):
    context = {
        'author_list' : models.Author.objects.all(),
    }

    return render(request,'app/author.html' , context)

def Author_detail(request,pk):
    obj = get_object_or_404(models.Author, pk=pk)
    context = {
        'author' : obj,
    }

    return render(request,'app/author_detail.html' , context)
