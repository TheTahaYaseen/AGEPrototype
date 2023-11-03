from django.db import models

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
