from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import ContentItem, Categories
from .serializers import ContentItemSerializer, CategoriesSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class UserContentItemViewset(viewsets.ModelViewSet):
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer
    permission_classes = [IsAuthenticated]

    def post_content(self, request):
        data = request.data
        user = request.user
        serializer_data = {
            'user': user.id,
            'title': data['title'],
            'body': data['body'],
            'summary': data['summary'],
            'document': data['document'],
        }

        serializer = ContentItemSerializer(data=serializer_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)

    def list_content(self, request):
        user = request.user
        queryset = ContentItem.objects.filter(user_id=user.id, is_active=True)
        serializer = ContentItemSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def get_content(self, request, content_id):
        user = request.user
        content_id = content_id
        try:
            queryset = ContentItem.objects.get(user_id=user.id, id=content_id)
            serializer = ContentItemSerializer(queryset)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": e})

    def update_content(self, request, content_id):
        user = request.user
        content_id = content_id
        try:
            instance = ContentItem.objects.get(user_id=user.id, id=content_id)
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data=e)

    def perform_update(self, serializer):
        serializer.save()

    # Deleting a data from a database is generally avoided. Hence this code deactivates it so its not visible to the user.
    def delete_content(self, request, content_id):
        user = request.user
        content_id = content_id
        try:
            instance = ContentItem.objects.get(user_id=user.id, id=content_id)
            instance.is_active = False
            instance.save()
            return Response(status=status.HTTP_200_OK, data={"contented Deleted."})
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={e})


class AdminContentItemViewset(viewsets.ModelViewSet):
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer
    permission_classes = [IsAuthenticated]

    def list_all_content(self, request):
        user = request.user
        print("I am here 1:", user.is_admin)
        if not user.is_admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        queryset = ContentItem.objects.all()
        serializer = ContentItemSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def list_content(self, request, user_id):
        user = request.user
        if not user.is_admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        queryset = ContentItem.objects.filter(user_id=user_id)
        serializer = ContentItemSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def get_content(self, request, user_id, content_id):
        user = request.user
        if not user.is_admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            queryset = ContentItem.objects.get(user_id=user_id, id=content_id)
            serializer = ContentItemSerializer(queryset)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": e})

    def update_content(self, request, user_id, content_id):
        user = request.user
        if not user.is_admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        instance = ContentItem.objects.get(user_id=user_id, id=content_id)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def delete_content(self, request, user_id, content_id):
        user = request.user
        if not user.is_admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            instance = ContentItem.objects.get(user_id=user_id, id=content_id)
            instance.is_active = False
            instance.save()
            return Response(status=status.HTTP_200_OK, data={"contented Deleted."})
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={e})


class ContentItemViewset(viewsets.ModelViewSet):
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer
    permission_classes = [IsAuthenticated]

    def list_content(self, request):
        query = request.GET.get('query', None)
        print('query:', query)
        if query:
            queryset = ContentItem.objects.filter(Q(Q(title__icontains=query) | Q(body__icontains=query) | Q(summary__icontains=query) | Q(categories__category__icontains=query)) & Q(is_active=True))
        else:
            queryset = ContentItem.objects.all()
        serializer = ContentItemSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    def post_content_category(self, request, content_id):
        data = request.data
        category_val = data['category']
        ser_data = {
            'contentitem_id': content_id,
            'category': category_val
        }
        serializer = CategoriesSerializer(data=ser_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)