from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

cards_dataset = [
    {"question": "Что такое PEP 8?",
     "answer": "PEP 8 — стандарт написания кода на Python.",
     "category": "Стандарты кода",
     "tags": ["PEP 8", "стиль", "форматирование"],
     "id_author": 1,
     "id_card": 1,
     "upload_date": "2023-01-15",
     "views_count": 100,
     "favorites_count": 25
     },
    {"question": "Как объявить список в Python?",
     "answer": "С помощью квадратных скобок: lst = []",
     "category": "Основы",
     "tags": ["списки", "основы"],
     "id_author": 2,
     "id_card": 2,
     "upload_date": "2023-01-20",
     "views_count": 150,
     "favorites_count": 30
     },
    {"question": "Что делает метод .append()?",
     "answer": "Добавляет элемент в конец списка.",
     "category": "Списки",
     "tags": ["списки", "методы"],
     "id_author": 2,
     "id_card": 3,
     "upload_date": "2023-02-05",
     "views_count": 75,
     "favorites_count": 20
     },
    {"question": "Какие типы данных в Python иммутабельные?",
     "answer": "Строки, числа, кортежи.",
     "category": "Типы данных",
     "tags": ["типы данных", "иммутабельность"],
     "id_author": 1,
     "id_card": 4,
     "upload_date": "2023-02-10",
     "views_count": 90,
     "favorites_count": 22
     },
    {"question": "Как создать виртуальное окружение в Python?",
     "answer": "С помощью команды: python -m venv myenv",
     "category": "Виртуальные окружения",
     "tags": ["venv", "окружение"],
     "id_author": 2,
     "id_card": 5,
     "upload_date": "2023-03-01",
     "views_count": 120,
     "favorites_count": 40
     }
]

info = {
    "users_count": 100500,
    "cards_count": 200600,
    # "menu": ['Главная', 'О проекте', 'Каталог']
    "menu": [
        {"title": "Главная страница",
         "url": "/",
         "url_name": "index"},
        {"title": "Информация о сайте и покупателях",
         "url": "/about/",
         "url_name": "about"},
        {"title": "Каталог товаров",
         "url": "/cards/catalog/",
         "url_name": "catalog"},
    ],
    "cards": cards_dataset  # Добавим в контекст шаблона информацию о карточках, чтобы все было в одном месте
}


def main(request):
    """Функция для отображения главной страницы
    будет возвращать рендер шаблона root/templates/main.html"""
    return render(request, "main.html", context=info)

def main(request):  
    """
    Представление рендерит шаблон base.html
    """
    return render(request, "base.html", context=info)

def about(request):
    """Функция для отображения страницы "О проекте"
    будет возвращать рендер шаблона /root/templates/about.html"""
    return render(request, 'about.html', context=info)


def get_goods_by_id(request, goods_id):
    card = None
    for c in cards_dataset:
        if c['id_card'] == goods_id:
            card = c
            break
    info['card'] = card
    if card:
        return render(request, 'goods/card_detail.html', context=info)
    return HttpResponse('Карточка не найдена', status=404)

def catalog(request):
    """Функция для отображения страницы "Каталог"""
    return render(request, 'goods/catalog.html', context=info)
