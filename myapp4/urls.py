from django.urls import path
from .views import form_app4, upload_image, upload_product_photo, product_detail


urlpatterns = [
    path('add/', form_app4, name='user_form'),
    path('add/upload/', upload_image, name='upload_image'),
    path('add/upload2/', upload_product_photo, name='upload_product_photo'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
]
