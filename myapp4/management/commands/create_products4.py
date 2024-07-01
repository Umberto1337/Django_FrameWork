from django.core.management.base import BaseCommand
from myapp4.models import Product


class Command(BaseCommand):
    help = "Create products."
    def handle(self, *args, **kwargs):
        for i in range(1, 2):
            product = Product(name=f'name{i}', description=f'description{i}', price=i * 0.3, quantity=i + 2)
            product.save()
            self.stdout.write(f'{product}') # Вывод информации в консоль