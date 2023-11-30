from django.db import models

class Categories(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'


class Dog(models.Model):
    name = models.CharField(verbose_name='Кличка', max_length=100)
    categories = models.ForeignKey(Categories, verbose_name='Порода', max_length=100, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фото', upload_to='dog/')
    date_of_birth = models.DateTimeField(verbose_name='Дата рождения', auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'

