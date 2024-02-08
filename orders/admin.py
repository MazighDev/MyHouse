from django.contrib import admin
from .models import  Order, OrderProduct, Payment
# Register your models here.

class OrderProductInline(admin.TabularInline):
    model= OrderProduct
    readonly_fields = ('payment','user','product','quantity','product_price', 'ordered')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display= ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'is_ordered','created_at']
    list_filter= ['is_ordered','created_at']
    search_fields=['order_number','first_name','last_name','phone','email']
    list_per_page= 20
    inlines = [OrderProductInline]
class PaymentAdmin(admin.ModelAdmin):
    list_display= ['payment_id', 'user', 'amount_paid', 'status']
    list_filter= ['user']
    list_per_page= 20

class OrderProductAdmin(admin.ModelAdmin):
    list_display= ['product','payment','user', 'created_at']
    list_filter= ['user']
    list_per_page= 20

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)
