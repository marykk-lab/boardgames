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
        ('Pending', 'В обработке'),
        ('Shipped', 'Отправлен'),
        ('Delivered', 'Доставлено'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=255,blank=True, null=True)
    stripe_checkout_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_product_id = models.CharField(max_length=255, blank=True, null=True)
    games = models.ForeignKey(Game, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
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
        return f"{self.user.username} - {self.games} - Paid: {self.has_paid}"

class UserPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
