from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    model = User  # Указывает, что используется модель User
    ordering = ('email',)  # Определяет порядок пользователей в списке (по email)
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')  # Поля, в списке юзеров в админке
    list_filter = ('is_staff', 'is_active')  # Поля для фильтрации списка пользователей
    fieldsets = (  # Определяет, как будут организованы поля в форме редактирования пользователя
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (  # Определяет, какие поля будут доступны при добавлении нового пользователя
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )
    search_fields = ('email',)  # Поля, по которым можно искать пользователей
    filter_horizontal = ('user_permissions',)  # Поля для горизонтального выбора, в этом случае user_permissions


admin.site.register(User, UserAdmin)
