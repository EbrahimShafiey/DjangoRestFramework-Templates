from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('',views.TodoViewSetApiView)

urlpatterns=[
    path('',views.all_todos),
    path('cbv/',views.Todo_Manage.as_view()),
    path('cbv/<int:todo_id>',views.Todo_CBV.as_view()),
    path('mixins/',views.TodoMixins.as_view()),
    path('mixins/<int:pk>',views.TodoMixinsDetail.as_view()),
    path('generics/',views.TodoGenericAPIView.as_view()),
    path('generics/<int:pk>',views.TodoGenericDetails.as_view()),
    path('viewsets/',include(router.urls)),
    path('users/',views.UserGenericAPIView.as_view())
]