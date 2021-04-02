from django.db import models
from django.urls import reverse


class Fact (models.Model) :
    title = models.CharField(max_length=150, verbose_name='наименование')
    content = models.TextField(blank=True, verbose_name='контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публикаций')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обнавлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='статус')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('read', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta :
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150 , verbose_name='Категорий')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta :
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'
        ordering = ['title']
