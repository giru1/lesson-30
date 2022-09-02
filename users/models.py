from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=500)
    lat = models.DecimalField(decimal_places=4, max_digits=6, null=True)
    lng = models.DecimalField(decimal_places=4, max_digits=6, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Админ"),
    ]

    role = models.CharField(max_length=500, choices=ROLES, default='member')
    age = models.PositiveIntegerField()
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'