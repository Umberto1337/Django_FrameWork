from django.core.management.base import BaseCommand
from myapp3.models import Order, Client


class Command(BaseCommand):
    help = "Creating orders for clients"

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()  # Получение всех клиентов из базы данных
        for client in clients:
            for i in range(1, 11):
                order = Order(client=client, total_amount=i * 3)  # Использование клиента из списка
                order.save()
                self.stdout.write(f'Order for {client.name} created')