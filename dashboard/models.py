from django.db import models

class Sale(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name