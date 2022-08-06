from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО', help_text='Введите ФИО')
    phone = models.CharField(max_length=20, verbose_name='Номер')
    email = models.EmailField(verbose_name='Электронка')


    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        db_table = 'customers'

    def __str__(self):
        return self.name


class Work(models.Model):
    address = models.CharField(max_length=20, verbose_name='Адрес')
    city = models.CharField(max_length=20, verbose_name='Город')
    company = models.CharField(max_length=20, verbose_name='Компания')
    postalZip = models.CharField(max_length=20, verbose_name='Почтовый индекс')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Покупатель')

    class Meta:
        verbose_name = 'Место работы'
        verbose_name_plural = 'Места работы'
        db_table = 'works'

    def __str__(self):
        return self.company

class Account(models.Model):
    pin = models.IntegerField(verbose_name='ПИн')
    acc_num = models.CharField(max_length=16)
    pan = models.CharField(max_length=16)
    cvv = models.IntegerField(unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Покупатель')

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
        db_table = 'accounts'

    def __str__(self):
        return self.acc_num
