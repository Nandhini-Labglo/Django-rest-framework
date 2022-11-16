from django.contrib import admin
from todo_api.models import Todo,Snippets,Product,Brand

# Register your models here.

class Todoadmin(admin.ModelAdmin):
    list_display = ['id','task','timestamp','completed','updated','user']
admin.site.register(Todo, Todoadmin)

class Snippetadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'code', 'linenos', 'language', 'style']
admin.site.register(Snippets, Snippetadmin)

class productadmin(admin.ModelAdmin):
    list_display = ['id','title','image','price','in_stock']
    search_fields = ('title','price')
    list_display_links =('price',)
    list_editable = ('title',)
    list_filter = ('price',)
admin.site.register(Product, productadmin)
admin.site.register(Brand)