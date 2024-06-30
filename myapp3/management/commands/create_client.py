from django.core.management.base import BaseCommand

from myapp3.models import Client


class Command(BaseCommand):
    help = "Create client."
    def handle(self, *args, **kwargs):
        client = Client(name="name2", email="email2", phone_number="phone_number2", address="address2")
        client.save()
        self.stdout.write(f'{client}') # Вывод информации в консоль