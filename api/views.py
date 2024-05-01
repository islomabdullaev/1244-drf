from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Book
from api.serializers import BookSerializer


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', "PUT", "DELETE", "PATCH"])
def book_detail(request, pk):
    if request.method == "GET":
        books = Book.objects.get(pk=pk)
        serializer = BookSerializer(books, many=False)
        return Response(serializer.data)