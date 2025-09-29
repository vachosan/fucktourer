from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Invoice
from .forms import InvoiceForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class InvoiceListView(ListView):
    model = Invoice
    template_name = "invoices/list.html"
    paginate_by = 20
    ordering = "-issue_date"

class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = "invoices/detail.html"

class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = "invoices/form.html"
    success_url = reverse_lazy("invoices:list")   
# Create your views here.
