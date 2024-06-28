from django.db import models


# Create your models here.
class Stock_Type(models.TextChoices):
    CPU_CHIP = 'CPU_CHIP'
    RAM = 'RAM'
    GPU_CHIP = 'GPU_CHIP'


# stock
class Stock(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=30, null=False)
    price = models.FloatField(default=0.0)
    type = models.TextField(
        choices=Stock_Type.choices,
        default=Stock_Type.CPU_CHIP
    )
    qty = models.IntegerField(default=0)
    price_trending_date = models.DateField(null=True)

