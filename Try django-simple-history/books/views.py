from django.shortcuts import render, redirect
from .models import Book

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        book = Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('book_list')
    return render(request, 'books/add_book.html')

def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.save()  # Save the changes
        return redirect('book_list')
    return render(request, 'books/edit_book.html', {'book': book})

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')
