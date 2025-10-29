from django.test import TestCase
from .models import Book
from .factories import AuthorFactory, BookFactory

class BookTestCase(TestCase):
    
    def test_create_author_and_book(self):
        # Create a single Author
        author = AuthorFactory()

        # Create a Book related to the above Author
        book = BookFactory(author=author)

        # Check that the Book's author is correct
        self.assertEqual(book.author.name, author.name)
        self.assertTrue(Book.objects.filter(author=author).exists())

    def test_create_multiple_books(self):
        # Create 10 books with random authors
        books = BookFactory.create_batch(10)
        
        # Check that 10 books were created
        self.assertEqual(len(books), 10)

    def test_author_with_multiple_books(self):
        # Create an Author and multiple related Books
        author = AuthorFactory()
        books = BookFactory.create_batch(5, author=author)

        # Check that the author has exactly 5 books
        self.assertEqual(author.books.count(), 5)
