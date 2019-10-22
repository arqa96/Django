from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

PHONE_CHOICES = [
    ('Apple', 'Apple'),
    ('Samsung','Samsung'),
    ('Xiaomi','Xiaomi'),
    ('LG','LG')
]
METRO_CHOICES = [
    ('Адмиралтейская', 'Адмиралтейская'),
    ('Новочеркасская', 'Новочеркасская'),
    ('Площадь Восстания', 'Площадь Восстания')
]


class Phone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField('Телефон', max_length=20, choices=PHONE_CHOICES)
    phone_model = models.CharField('Модель Телефона', max_length=10)
    image_field = models.ImageField('Картинка', default='default.png', upload_to='phone_pics')
    price = models.IntegerField('Цена')
    name = models.CharField('Имя', max_length=15, blank=True, null=True)
    metro = models.CharField('Станция Метро', max_length=20, choices=METRO_CHOICES)
    comments = models.TextField('Комментарии Пользователя', blank = True, null=True)
    phone_number = models.CharField('Номер телефона', max_length=11, help_text='Input your phone number in format 79XXXXXXXXX')
    pub_date = models.DateTimeField('Дата Публикации', default=timezone.now)

    def valid_phone_number(self):
        num = self.phone_number
        return '+%s(%s%s%s)%s%s%s-%s%s-%s%s' % tuple(num)

    def __str__(self):
        return f'{self.phone} {self.phone_model}'

    def get_absolute_url(self):
        return reverse('phone-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'информация'
        verbose_name_plural = 'информация'
