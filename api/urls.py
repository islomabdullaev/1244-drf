from django.urls import path
from api.views import book_list, book_detail

app_name = 'api'

urlpatterns = [
    path('books/', book_list, name='books'),
    path('books/<int:pk>/', book_detail, name='book_detail')
]