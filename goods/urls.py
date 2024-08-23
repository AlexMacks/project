from django.urls import path

from . import views

urlpatterns = [
    path("", views.main),
    path("<int:goods_id>", views.get_goods_by_id),
]