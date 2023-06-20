from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="crud"),
    path("add", views.add, name="add_tamu"),
    path("update/<int:id>", views.update, name="update_tamu"),
    path("delete/<int:id>", views.delete, name="delete_tamu"),
]
