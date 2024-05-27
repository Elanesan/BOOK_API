from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Book
from rest_framework.response import Response
from .serializers import *
# Create your views here.

class BookApiView(APIView):
    serializer_class=BookSerializers
    def get(self,request):
        allBooks=Book.objects.all().values()
        return Response({"Message":"List of Books","Book List":allBooks})

    def post(self,request):
        print("Request data is : ",request.data)
        serializer_obj=BookSerializers(data=request.data)
        if(serializer_obj.is_valid()):

        
            Book.objects.create(id=serializer_obj.data.get("id"),
                                title=serializer_obj.data.get("title"),
                                author=serializer_obj.data.get("author")
                                )
        New_Book=Book.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Book Added!","Book List":New_Book})






