from django.urls import re_path
from .views import login_view

urlpatterns = [
    re_path(r'^.*$', login_view, name='login_view'),  # Перехватывает все URL
]
