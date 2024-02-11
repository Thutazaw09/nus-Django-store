from django.urls import path
from . import views

app_name = "items"
urlpatterns = [
    path('<int:pk>/', views.detail ,name="store-detail"),
    path('new/',views.newItem,name="store-new"),
]
