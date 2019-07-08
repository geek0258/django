from django.shortcuts import render
from comp.models import Book
from comp.forms import BookForm

def saveBook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                form.save();
            except:
                pass
    else:
        form = BookForm()
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})

def getAll(request):
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})