from django.urls import path
from .views import Mailgb, UserList, CreateUser

urlpatterns = [
    path('', Mailgb.as_view()),
    path('index/', UserList.as_view(), name="index"),
    path("reg/", CreateUser.as_view(), name='reg')
]