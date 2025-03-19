from django.urls import include, path
from .views import index, filegetview, filepostview

urlpatterns = [
    path('', index, name="view"),
    path('f/create/', filepostview, name="filepostview"),
    path('f/<str:url>/', filegetview, name="filegetview"),
]
