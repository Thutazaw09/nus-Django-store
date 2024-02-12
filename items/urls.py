from django.urls import path
from . import views

app_name = "items"
urlpatterns = [
    path('<int:pk>/', views.detail ,name="items-detail"),
    path('new/',views.newItem,name="items-new"),
    path('<int:pk>/delete.', views.delete ,name="items-delete"),
    path('<int:pk>/edit.', views.editItem ,name="items-edit"),
]
