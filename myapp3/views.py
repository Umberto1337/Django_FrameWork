from datetime import timedelta
from django.utils import timezone

from django.http import HttpResponse
import logging

logging.basicConfig(filename='./log/app.log', level=logging.INFO)

from django.shortcuts import render
from .models import Client, Order


def client_orders(request, client_id):
    client = Client.objects.get(pk=client_id)

    seven_days_ago = timezone.now() - timedelta(days=7)
    orders_last_7_days = Order.objects.filter(client=client, order_date__gte=seven_days_ago).order_by('-order_date')

    thirty_days_ago = timezone.now() - timedelta(days=30)
    orders_last_30_days = Order.objects.filter(client=client, order_date__gte=thirty_days_ago).order_by('-order_date')

    year_ago = timezone.now() - timedelta(days=365)
    orders_last_365_days = Order.objects.filter(client=client, order_date__gte=year_ago).order_by('-order_date')

    context = {
        'client': client,
        'orders_last_7_days': orders_last_7_days,
        'orders_last_30_days': orders_last_30_days,
        'orders_last_365_days': orders_last_365_days,
    }

    return render(request, 'orders.html', context)


def index2(request):
    html = """
        <html>
        <head>
            <title>Страница myapp3</title>
        </head>
        <body>
            <h1>Добро пожаловать на страницу myapp3</h1>
            <p>Здесь вы найдете много интересного контента.</p>
        </body>
        </html>
        """
    log_data = "Посещена страница myapp3"
    logging.info(log_data)

    return HttpResponse(html)