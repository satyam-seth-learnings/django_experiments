import getpass
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.core.validators import validate_email

# Custom Command with Prompt No Arguments


class Command(BaseCommand):
    help = "Create normal user with prompt"

    def handle(self, *args, **kwargs):
        username = input("Username: ")
        email = input("Email: ")
        password = getpass.getpass("Password: ")
        password2 = getpass.getpass("Password (again): ")

        if password != password2:
            self.stdout.write(self.style.ERROR("Error: Your passwords didn’t match."))
            return
        try:
            validate_email(email)
        except ValidationError:
            self.stdout.write(self.style.ERROR("Error: Enter a valid email address."))
            return
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.ERROR("Error: A user with that username already exists.")
            )
            return
        if User.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.ERROR("Error: A user with that email already exists.")
            )
            return
        try:
            User.objects.create_user(username=username, email=email, password=password)
            self.stdout.write(
                self.style.SUCCESS(f"User {username} created successfully.")
            )
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f"Error: {e.message_dict}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {str(e)}"))
