from django import forms
from comp.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"