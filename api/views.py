# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Book
from api.serializers import BookSerializer


# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == "GET":
#         books = Book.objects.filter(is_active=True)
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(request.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', "PUT", "DELETE", "PATCH"])
# def book_detail(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response({"message": "not found !"})

#     if request.method == "GET":
#         serializer = BookSerializer(book, many=False)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializer = BookSerializer(instance=book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
#     elif request.method == "DELETE":
#         book.delete()
#         content = {
#             "message": "Deleted Successfully !"
#         }
#         return Response(data=content, status=status.HTTP_204_NO_CONTENT)
    
#     elif request.method == "PATCH":
#         serializer = BookSerializer(instance=book, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.filter(is_active=True)
        serializer = BookSerializer(instance=books, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serilaizer = BookSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(data=serilaizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)
