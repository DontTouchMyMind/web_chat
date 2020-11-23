from django.urls import path
from .views import signup_view, index, login_view, room, chat

urlpatterns = [
    path('webchat', chat, name='webchat'),
    path('account/create/', signup_view, name='signup'),
    path('', login_view, name='login'),
    path('<str:room_name>/', room, name='room'),



]
