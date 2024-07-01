from django.contrib import admin
from .models import Client, Product, Order



@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity']
    ordering = ['description', '-quantity']
    list_filter = ['added_date', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта  (description)'
    actions = [reset_quantity]

    # fields = ['name', 'description', 'added_date']
    # readonly_fields = ['added_date', 'price']
    readonly_fields = ['added_date']  # Удалено поле 'price' из readonly_fields
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields':['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Дата и Время',
            {
                'description': 'Дата и Время Сформировано автоматически',
                'fields': ['added_date'],
            }
        ),
    ]

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone_number']
    search_fields = ['name', 'email', 'phone_number']
    list_filter = ['name', 'email']
    fieldsets = [
        (
            None,
            {
                'fields': ['name', 'email', 'phone_number'],
            },
        ),
    ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'total_amount', 'order_date']
    search_fields = ['client__name', 'product__name']
    list_filter = ['order_date']
    fieldsets = [
        (
            None,
            {
                'fields': ['client', 'order_date'],
            },
        ),
    ]



admin.site.register(Client, ClientAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order, OrderAdmin)