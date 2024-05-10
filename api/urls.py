from django.urls import path
from api.views import BookListAPIView

app_name = 'api'

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='books'),
    # path('books/<int:pk>/', book_detail, name='book_detail')
]