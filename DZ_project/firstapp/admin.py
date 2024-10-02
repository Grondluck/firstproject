from django.contrib import admin
from firstapp.models import clients, products, tags

# Register your models here.
class conf_clients(admin.ModelAdmin):
    list_display = "nickname name lastname purchase_history date_of_last_purchase dor".split(" ")

class conf_products(admin.ModelAdmin):
    list_display = "name count count_left price_selling price_purchase doc discount".split(" ")

class conf_tags(admin.ModelAdmin):
    list_display = "tag tag_RU".split(" ")

admin.site.register(clients, conf_clients)
admin.site.register(products, conf_products)
admin.site.register(tags, conf_tags)