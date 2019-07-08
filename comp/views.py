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

def updateBook(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST, instance = book)
    if form.is_valid():
        try:
            form.save();
        except:
            pass
        return redirect("")
    return render(request, "edit.html", {"book": book})

def deleteBook(request, id):
    book = Book.objects.get(id=id)
    if book:
        try:
            book.delete()
        except:
            pass
        return redirect("")
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})