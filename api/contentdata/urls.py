from django.urls import path
from .views import UserContentItemViewset, AdminContentItemViewset, CategoryViewset, ContentItemViewset

urlpatterns = [
    path('content/', UserContentItemViewset.as_view(
        {
            'post': 'post_content',
            'get': 'list_content'
        }
    ),
         name='create_content'),

    path('content/<uuid:content_id>', UserContentItemViewset.as_view(
        {
            'get': 'get_content',
            'patch': 'update',
            'delete': 'delete_content'
        }
    )),

    path('content/<uuid:content_id>/add_category', CategoryViewset.as_view(
        {
            'post': 'post_content_category'
        }
    )),

    # Admin URLS
    path('users/', AdminContentItemViewset.as_view(
        {
            'get': 'list_all_content'
        }
    ),
         name='list_all_content'),

    path('users/<uuid:user_id>/content', AdminContentItemViewset.as_view(
        {
            'get': 'list_content',
        }
    )),

    path('users/<uuid:user_id>/content/<uuid:content_id>', AdminContentItemViewset.as_view(
        {
            'get': 'get_content',
            'patch': 'update_content',
            'delete': 'delete_content'
        }
    )),

    path('search/content/', ContentItemViewset.as_view(
        {
            'get': 'list_content',
        }
    )),

]
