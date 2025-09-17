from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    review = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    rating = models.PositiveIntegerField()
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_game", "Can add game"),
            ("can_delete_game", "Can delete game"),
            ("can_edit_game", "Can edit game")
        ]
        
class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=255,blank=True, null=True)
    stripe_checkout_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_product_id = models.CharField(max_length=255, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100, default='default')
    city = models.CharField(max_length=100, default='default')
    address = models.CharField(max_length=100, default='default')
    currency = models.CharField(max_length=3, default='usd')
    email = models.CharField(max_length=100, default='default')
    phone = models.CharField(max_length=15, default='default')
    notes = models.CharField(max_length=100, default='default')
    zip = models.CharField(max_length=10, default='default')
    full_name = models.CharField(max_length=30, default='default')
    has_paid = models.BooleanField(default=False)

    def __str__(self):
        items = self.orderitem_set.all()
        if items:
            return f"{self.user.username} - {items[0].game.title} (+{items.count()-1} more) - Paid: {self.has_paid}"
        return f"{self.user.username} - No items - Paid: {self.has_paid}"
    def games_summary(self):
        return ", ".join(
            f"{item.game.title} x{item.count}" for item in self.orderitem_set.all()
        )
    def status_label(self):
        status_map = {
            'Pending': '🕓 Pending',
            'Shipped': '📦 Shipped',
            'Delivered': '✅ Delivered',
        }
        return status_map.get(self.status, self.status)
    games_summary.short_description = "Games Ordered"


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.game.title} x{self.count}"


class UserPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
