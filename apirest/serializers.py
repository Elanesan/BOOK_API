from rest_framework import serializers
from django.db import models

class BookSerializers(serializers.Serializer):
    id=serializers.IntegerField(label="Enter the Book ID: ")
    title=serializers.CharField(label="Enter the Book Title: ")
    author=serializers.CharField(label="Enter the Author Name: ")