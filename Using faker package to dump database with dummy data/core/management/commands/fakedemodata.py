from faker import Faker
from django.core.management.base import BaseCommand
from core.models import DemoModel

fake = Faker()


class Command(BaseCommand):
    help = "Dump fake data to Demo model"

    def add_arguments(self, parser):
        parser.add_argument("no_of_data", type=int, help="Number of data to be added")

    def handle(self, *args, **kwargs):
        no_of_data = kwargs["no_of_data"]
        for _ in range(no_of_data):
            DemoModel.objects.create(
                name=fake.name(),
                address=fake.address(),
                phone_number=fake.phone_number(),
            )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully dumped {no_of_data} dummy data.")
        )
