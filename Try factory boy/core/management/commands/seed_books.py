from django.core.management.base import BaseCommand
from core.factories import AuthorFactory, BookFactory

class Command(BaseCommand):
    help = 'Seed the database with authors and books'

    def handle(self, *args, **kwargs):
        # Create 5 authors, each with 3 books
        for _ in range(5):
            author = AuthorFactory()
            BookFactory.create_batch(3, author=author)
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
