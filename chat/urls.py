from django.urls import path
from .views import signup_view, index, login_view, room, test

urlpatterns = [
    path('index/', index, name='index'),
    path('account/create/', signup_view, name='signup'),
    path('', login_view, name='login'),
    path('<str:room_name>/', room, name='room'),
    path('<str:recipient>/', test, name='test'),




]
