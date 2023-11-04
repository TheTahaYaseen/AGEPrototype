from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteSpecificationModel(models.Model):
    type = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class SiteSpecificationsDetailModel(models.Model):
    specification_of = models.ForeignKey(SiteSpecificationModel, on_delete=models.CASCADE)
    detail_type = models.CharField(max_length=255)
    detail = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class UserQuery(models.Model):
    query_user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    admin_response = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class ProductCategory(models.Model):
    category = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_category = models.ForeignKey("ProductCategory", on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class ProductMedia(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    media_file = models.FileField(upload_to="product_media/")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

