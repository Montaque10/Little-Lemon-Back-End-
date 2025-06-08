from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    description = models.TextField(max_length=1000, default='')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='menu_items/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=255, default='')
    phone = models.CharField(max_length=20, default='')
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )
    guests = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        default=1
    )
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-reservation_date', 'reservation_slot']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.reservation_date}'

class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    menu_items = models.ManyToManyField(MenuItem, related_name='menus')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name