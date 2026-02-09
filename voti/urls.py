from django.urls import path
from .views import index, view_a, view_b

app_name = 'voti'

urlpatterns = [
    path('', index, name="index"),
    path('view_a', view_a, name="view_a"),
    path('view_b', view_b, name="view_b"),
]