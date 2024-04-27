from django.db import models


class Person(models.Model):

    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Product(models.Model):

    status_choices = (('draft', 'Draft'), ('published', 'Published'))

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=status_choices, default='draft')

    available = models.BooleanField(default=True)
    numbers = models.PositiveIntegerField()
    discount = models.FloatField(default=0)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.name
