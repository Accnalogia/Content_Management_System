from .views import LoginViewset, RegisterViewset
from django.urls import path

urlpatterns = [
    path('register/', RegisterViewset.as_view(
        {
            'post': 'post_register'
        }
    ), name='register'),

    path('login/', LoginViewset.as_view(
        {
            'post': 'post_login'
        }
    ), name='login')
]