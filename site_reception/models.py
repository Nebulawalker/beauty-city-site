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

    appointment_date = models.DateField(
        verbose_name='Дата записи',
        null=True
    )

    TIME_SLOTS = [
        ('10-00', 'Утро 10-00'),
        ('10-30', 'Утро 10-30'),
        ('11-00', 'Утро 10-30'),
        ('11-30', 'Утро 10-30'),
        ('12-00', 'День 12-00'),
        ('12-30', 'День 12-30'),
        ('13-00', 'День 13-00'),
        ('13-30', 'День 13-30'),
        ('14-00', 'День 14-00'),
        ('14-30', 'День 14-30'),
        ('15-00', 'День 15-00'),
        ('15-30', 'День 15-30'),
        ('16-00', 'День 16-00'),
        ('16-30', 'День 16-30'),
        ('17-00', 'Вечер 17-00'),
        ('17-30', 'Вечер 17-30'),
        ('18-00', 'Вечер 18-00'),
        ('18-30', 'Вечер 18-30'),
        ('19-00', 'Вечер 19-00'),
        ('19-30', 'Вечер 19-30'),
        ('20-00', 'Вечер 20-00'),
        ('20-30', 'Вечер 20-30'),
        ('21-00', 'Вечер 21-00'),
        ('21-30', 'Вечер 21-30'),
    ]

    appointment_time = models.CharField(
        verbose_name='Время записи',
        choices=TIME_SLOTS,
        max_length=20,
        null=True
    )

    STATUS_CHOICES = (
        ('booked', 'Забронирован'),
        ('payed', 'Оплачен'),
        ('done', 'Выполнен/Отменен'),
    )

    appointment_status = models.CharField(
        verbose_name='Статус записи',
        choices=STATUS_CHOICES,
        max_length=20,
        default='booked'

    )
    # def __str__(self):
    #     return f'{self.created_at}, {self.ser}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
