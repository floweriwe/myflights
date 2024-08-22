from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models
from django.db import IntegrityError


class MyUserManager(BaseUserManager):
    """
    Менеджер для пользовательской модели User.
    Содержит методы для создания обычных пользователей и суперпользователей.
    """

    def create_user(self, email: str, password=None, **kwargs):
        """
        Создает и сохраняет обычного пользователя с указанным email и паролем.
        """
        try:
            # проверка, указан ли email
            if not email:
                raise ValueError('Поле Email должно быть заполнено')
            # нормализация email
            email = self.normalize_email(email)
            # создание объекта пользователя с указанным email и доп.полями
            username = email.split('@')[0]  # username = 1-я часть Email'а до знака @
            user = self.model(email=email, username=username, **kwargs)
            # задается пароль для пользователя
            user.set_password(password)
            # сохраняем пользователя в базе данных
            user.save(using=self._db)
            return user

        except ValueError as ve:
            print(f"Ошибка создания пользователя: {ve}")
        except IntegrityError as ie:
            print(f"Ошибка интеграции данных: {ie}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

    def create_superuser(self, email, password=None, **kwargs):
        """
        Создает и сохраняет суперпользователя с указанным email и паролем.
        """
        try:
            # Устанавливаются значения по умолчанию для суперпользователя
            kwargs.setdefault('is_staff', True)
            kwargs.setdefault('is_superuser', True)

            # Если суперпользователь не является staff или superuser, выбрасываем ошибку
            if kwargs.get('is_staff') is not True:
                raise ValueError('Суперпользователь должен иметь is_staff=True.')
            if kwargs.get('is_superuser') is not True:
                raise ValueError('Суперпользователь должен иметь is_superuser=True.')

            # Используется метод create_user для создания суперпользователя
            return self.create_user(email, password, **kwargs)

        except ValueError as ve:
            print(f"Ошибка создания суперпользователя: {ve}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
