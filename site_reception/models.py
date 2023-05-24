from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    name = models.CharField(
        verbose_name='Имя клиента',
        max_length=100,
    )
    phone_number = PhoneNumberField(
        verbose_name='Телефон клиента'
    )

    def __str__(self):
        return f'{self.name}, телефон {self.phone_number}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Service(models.Model):
    title = models.CharField(
        verbose_name='Услуга',
        max_length=50,
    )
    duration = models.IntegerField(
        verbose_name='Продолжительность услуги (мин.)',
        default=30
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=8,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Master(models.Model):
    name = models.CharField(
        verbose_name='Имя мастера',
        max_length=50
    )

    service = models.ManyToManyField(
        Service,
        verbose_name='Услуги предоставляемые мастером',
        related_name='services'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class Saloon(models.Model):
    title = models.CharField(
        verbose_name='Название салона',
        max_length=25
    )
    address = models.CharField(
        verbose_name='Адрес салона',
        max_length=200
    )

    master = models.ManyToManyField(
        Master,
        verbose_name='Мастера в салоне',
        related_name='saloons',
        blank=True
    )

    def __str__(self):
        return f'{self.title}, Адрес: {self.address}'

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'


class Order(models.Model):
    saloon = models.ForeignKey(
        Saloon,
        verbose_name='Выбранный салон',
        related_name='saloon',
        on_delete=models.RESTRICT
    )
    service = models.ForeignKey(
        Service,
        verbose_name='Выбранная услуга',
        related_name='service',
        on_delete=models.RESTRICT
    )
    client = models.ForeignKey(
        Client,
        verbose_name='Клиент',
        related_name='client',
        on_delete=models.RESTRICT
    )
    master = models.ForeignKey(
        Master,
        verbose_name='Выбранный мастер',
        related_name='master',
        on_delete=models.RESTRICT
    )
    created_at = models.DateTimeField(
        verbose_name='Когда создана запись',
        default=timezone.now,
        db_index=True,
        editable=False
    )

    def __str__(self):
        return f'{self.title}, {self.address}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
