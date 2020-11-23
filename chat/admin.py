from django.contrib import admin

from django.contrib import admin

from chat.models import User
from .models import Message


class ChatAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'status']
    actions = ['ban_user', 'unban_user']

    def ban_user(self, request, queryset):
        queryset.update(status='b')

    ban_user.short_description = "Mark selected users as banned"

    def unban_user(self, request, queryset):
        queryset.update(status='a')

    unban_user.short_description = "Mark selected users as unbanned"

    # def block_user(self, request, queryset):
    #     queryset.update(is_active=False)
    #
    # block_user.short_description = "Deactivate users"
    #
    # def unblock_user(self, request, queryset):
    #     queryset.update(is_active=True)
    #
    # unblock_user.short_description = "Activate users"



admin.site.register(Message)
admin.site.register(User, ChatAdmin)
