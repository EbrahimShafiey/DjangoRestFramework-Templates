from tkinter import NO
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer, UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

User=get_user_model()

#region CustomPaginationSize
class CustomPageSize(PageNumberPagination):
    page_size=3
#endregion

#region Func base view
@api_view(['GET','POST'])
def all_todos(request:Request):
    if request.method == 'GET':
        todos=Todo.objects.order_by('priority').all()
        todo_serializer=TodoSerializer(todos,many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method =='POST':
        serializer = TodoSerializer(data=request.data) # type: ignore
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
    return Response(None,status.HTTP_400_BAD_REQUEST)
#endregion

#region Class base view
class Todo_Manage(APIView):
    def get(self, request:Request):
        todos=Todo.objects.order_by('priority').all()
        todo_serializer=TodoSerializer(todos,many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    
    def post(self, request:Request):
        serializer = TodoSerializer(data=request.data) # type: ignore
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(None,status.HTTP_400_BAD_REQUEST)

class Todo_CBV(APIView):
    def get_Object(self, todo_id:int):
        todo=Todo.objects.get(pk=todo_id)
        return todo
    
    def get(self,request:Request, todo_id:int):
        todos=self.get_Object(todo_id)
        todo_serializer=TodoSerializer(todos)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    
    def put(self, request:Request, todo_id:int):
        todo=self.get_Object(todo_id)
        serializer=TodoSerializer(todo,data=request.data) # type: ignore
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(None, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request:Request, todo_id:int):
        todo=self.get_Object(todo_id)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
#endregion        

#region Mixins
class TodoMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset=Todo.objects.order_by('priority').all()
    serializer_class=TodoSerializer
    def get(self, request: Request):
        return self.list(request)
    
    def post(self, request:Request):
        return self.create(request)
    
class TodoMixinsDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset=Todo.objects.order_by('priority').all()
    serializer_class=TodoSerializer
    def get(self, request:Request,pk):
        return self.retrieve(request,pk)
    
    def put(self, request:Request, pk):
        return self.update(request, pk)
    
    def delete(self, request:Request, pk):
        return self.destroy(request, pk)
#endregion

#region Generics
class TodoGenericAPIView(generics.ListCreateAPIView):
    queryset=Todo.objects.order_by('priority').all()
    serializer_class=TodoSerializer
    #استفاده از سیستم بیسیک برای هویت سنجی
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class TodoGenericDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.order_by('priority').all()
    serializer_class=TodoSerializer
#endregion

#region ViewSets
class TodoViewSetApiView(viewsets.ModelViewSet):
    queryset=Todo.objects.order_by('priority').all()
    serializer_class=TodoSerializer
    #استفاده از لیمیتر دستی  در نمایش این کلاس
    pagination_class=CustomPageSize
#endregion

#region users (Nested Serializers)
class UserGenericAPIView(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
#endregion

