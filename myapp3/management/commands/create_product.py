from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = "Create client."
    def handle(self, *args, **kwargs):
        product = Product(name='name3', description='description3', price=0.3, quantity=13)
        product.save()
        self.stdout.write(f'{product}') # Вывод информации в консоль