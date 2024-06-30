from django.shortcuts import render
from django.http import HttpResponse
import logging

logging.basicConfig(filename='./log/app.log', level=logging.INFO)


def index(request):
    html = """
        <html>
        <head>
            <title>Добро пожаловать на мой первый сайт!</title>
        </head>
        <body>
            <h1>Добро пожаловать на главную страницу</h1>
            <p>Здесь вы найдете много интересного контента.</p>
        </body>
        </html>
        """
    log_data = "Посещена главная страница"
    logging.info(log_data)

    return HttpResponse(html)

def about(request):
    html = """
        <html>
        <head>
            <title>Информация обо мне</title>
        </head>
        <body>
            <h1>Обо мне</h1>
            <p>Привет, меня зовут Алексей и это мой первый Django-сайт.</p>
        </body>
        </html>
        """
    log_data = "Посещена страница 'о себе'"
    logging.info(log_data)

    return HttpResponse(html)