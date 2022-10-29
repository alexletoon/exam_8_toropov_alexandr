from django.db import models
from django.db.models import TextChoices
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


class Choice(TextChoices):
    ELECTRONICS = 'ELEC', 'Электроника'
    GROCERIES = 'GROS', 'Бакалея'
    PETS = 'PETS', 'Зоотовары'
    ALCOHOL = 'ALC', 'Алкоголь'
    OTHER = 'OTHER', 'Разное'


class Product(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=100, null=False,blank=False)
    category = models.TextField(verbose_name='Категория', max_length=20, null=False, blank=False, choices=Choice.choices, default=Choice.OTHER)
    description = models.TextField(verbose_name="Описание", max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='product_img', verbose_name='Фото')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)


    def __str__(self) -> str:
        return f'{self.name}'


class Review(models.Model):
    author = models.ForeignKey(to=get_user_model(), verbose_name='Автор', related_name='author_reviews', null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(to='review_app.Product', verbose_name='Продукт', related_name='product_reviews', null=False, blank=False, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Отзыв', max_length=3000, null=False, blank=True)
    rating = models.PositiveSmallIntegerField(verbose_name='Оценка', null=False, blank=False, validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self) -> str:
        return f'{self.author}, {self.rating}'

