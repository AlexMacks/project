# goods/urls.py
from django.urls import path
from . import views

# будет иметь префикс в urlах /goods/
urlpatterns = [
    path("<int:goods_id>/detail", views.get_goods_by_id, name="get_goods_by_id"),
    path('catalog/', views.catalog, name='catalog'),  # Общий каталог всех карточек
]