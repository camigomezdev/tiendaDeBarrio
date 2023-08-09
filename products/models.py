from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=10,
                                 validators=[MinLengthValidator(10)])
    category = models.ForeignKey(
        'products.Category', on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(
        'products.Brand', on_delete=models.CASCADE, related_name='products')
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='media/fotos', max_length=100)
    description = models.TextField()

    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    @property
    def get_price(self):
        if self.discount:
            return self.discount
        if self.category.discount:
            total = self.price - self.price * self.category.discount
            return total
        return self.price

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.name} | {self.brand}'


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(
        'products.Product', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
