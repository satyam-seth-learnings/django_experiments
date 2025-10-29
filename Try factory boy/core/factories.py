import factory
from .models import Author, Book


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker('name')
    bio = factory.Faker('paragraph')

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('sentence')
    publication_date = factory.Faker('date_this_decade')
    author = factory.SubFactory(AuthorFactory)  # Creates an Author if not provided
