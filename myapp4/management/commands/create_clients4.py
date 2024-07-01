from django.core.management.base import BaseCommand
from myapp4.models import Client


class Command(BaseCommand):
    help = "Create client."
    def handle(self, *args, **kwargs):
        for i in range(2):
            client = Client(name=f"name{i}", email=f"email{i}@email.ru", phone_number=f"100{i}", address=f"address{i}")
            client.save()
            self.stdout.write(f'{client}')  # Вывод информации в консоль