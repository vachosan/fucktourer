from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Invoice

class InvoiceListView(ListView):
    model = Invoice
    paginate_by = 20
    ordering = "-issue_date"

class InvoiceDetailView(DetailView):
    model = Invoice
# Create your views here.
