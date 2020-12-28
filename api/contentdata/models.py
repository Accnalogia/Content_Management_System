"""Models for ContentData App"""
from django.db import models
from api.core.models import CMSUser, BaseModelMixin


class ContentItem(BaseModelMixin):
    user = models.ForeignKey(CMSUser, on_delete=models.CASCADE, related_name='content_item')
    title = models.CharField(max_length=30, null=False)
    body = models.TextField(max_length=300, null=False)
    summary = models.CharField(max_length=60, null=False)
    document = models.FileField(upload_to='content/file', null=False)
    is_active = models.BooleanField(default=True)


class Categories(BaseModelMixin):
    contentitem = models.ForeignKey(ContentItem, on_delete=models.CASCADE, related_name='categories')
    category = models.CharField(max_length=30)
