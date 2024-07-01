from django.db import models

from myapp3.models import Product, Order


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Обзор для {self.product.name} by {self.user_name}'


class OrderComment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий к заказу {self.order.id} by {self.user_name}'