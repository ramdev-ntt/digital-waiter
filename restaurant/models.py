from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2) # Better than Float for currency
    
    def __str__(self):
        return f"{self.name} - ${self.price}"

class Order(models.Model):
    # We use ManyToMany because one order has many items, 
    # and one item can belong to many orders.
    items = models.ManyToManyField(MenuItem) 
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - ${self.total_price}"