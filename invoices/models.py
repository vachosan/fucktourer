from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=255)
    ico = models.CharField("IČO", max_length=20, blank=True)
    dic = models.CharField("DIČ", max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, default="Česká republika", blank=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    DRAFT = "draft"
    ISSUED = "issued"
    PAID = "paid"
    CANCELLED = "cancelled"
    STATUS_CHOICES = [
        (DRAFT, "Návrh"),
        (ISSUED, "Vystavená"),
        (PAID, "Zaplacená"),
        (CANCELLED, "Stornovaná"),
    ]

    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name="invoices")
    number = models.CharField("Číslo faktury", max_length=50, unique=True)
    issue_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    variable_symbol = models.CharField("Variabilní symbol", max_length=20, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DRAFT)
    note = models.TextField(blank=True)
    vat_rate = models.DecimalField("DPH %", max_digits=4, decimal_places=2, default=0)  # např. 21.00
    bank_account = models.CharField("Číslo účtu", max_length=64, blank=True)

    @property
    def subtotal(self):
        return sum(i.total for i in self.items.all())

    @property
    def vat_amount(self):
        return (self.subtotal * self.vat_rate / 100) if self.vat_rate else 0

    @property
    def total(self):
        return self.subtotal + self.vat_amount

    def __str__(self):
        return f"{self.number} – {self.client.name}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")
    description = models.CharField("Popis", max_length=255)
    quantity = models.DecimalField("Množství", max_digits=10, decimal_places=2, default=1)
    unit = models.CharField("Jednotka", max_length=20, default="ks")
    unit_price = models.DecimalField("Cena/jedn. (bez DPH)", max_digits=12, decimal_places=2)

    @property
    def total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.description} ({self.quantity} {self.unit})"
