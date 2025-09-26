from django.urls import path
from .views import InvoiceListView, InvoiceDetailView

app_name = "invoices"

urlpatterns = [
    path("", InvoiceListView.as_view(), name="list"),
    path("<int:pk>/", InvoiceDetailView.as_view(), name="detail"),
]
