from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    categories = models.ManyToManyField("Category", related_name="products", blank=True)
    tags = models.ManyToManyField("Tag", related_name="products", blank=True)

class Category(models.Model):
    name = models.CharField(max_length=200)

class Tag(models.Model):
    name = models.CharField(max_length=200)