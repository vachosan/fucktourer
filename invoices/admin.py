from django.contrib import admin
from .models import Client, Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ["name", "ico", "dic", "email"]

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["number", "client", "issue_date", "due_date", "status", "total"]
    list_filter = ["status", "issue_date", "due_date"]
    search_fields = ["number", "client__name", "variable_symbol"]
    inlines = [InvoiceItemInline]
# Register your models here.
