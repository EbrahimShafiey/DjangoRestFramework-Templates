from dataclasses import field
from pyexpat import model
from tkinter.tix import Tree
from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model

user=get_user_model()


class TodoSerializer(serializers.ModelSerializer):
    def validate_priority(self, priority):
        if priority<10 or priority>20:
            raise serializers.ValidationError('insert (10<x<20)')
        return priority

    class Meta:
        model=Todo
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    todos=TodoSerializer(read_only=True, many=True)

    class Meta:
        model=user
        fields='__all__'