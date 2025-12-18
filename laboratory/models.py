from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('S', 'Холост/Не замужем'),
        ('M', 'Женат/Замужем'),
        ('D', 'Разведен(а)'),
        ('W', 'Вдовец/Вдова'),
    ]

    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Пол")
    age = models.PositiveIntegerField(verbose_name="Возраст")
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES, verbose_name="Семейное положение")
    has_children = models.BooleanField(default=False, verbose_name="Наличие детей")
    position = models.CharField(max_length=255, verbose_name="Должность")
    academic_degree = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ученая степень")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name="Добавлен пользователем")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ['full_name']
