from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        #fields = ['name', 'desc', 'book_image', 'price']
        fields = '__all__'