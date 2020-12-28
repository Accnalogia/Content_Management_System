""" Serializers for Models in Core App """
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import ContentItem, Categories
from api.core.models import CMSUser


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

    def to_internal_value(self, data):
        return{
            'contentitem_id': data['contentitem_id'],
            'category': data['category'],
        }


class ContentItemSerializer(ModelSerializer):
    categories = CategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = ContentItem
        fields = (
            'id',
            'create_date',
            'update_date',
            'title',
            'body',
            'summary',
            'document',
            'is_active',
            'user',
            'categories'
        )
