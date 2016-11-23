# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class TruckModel(models.Model):
    title = models.CharField(max_length=16, verbose_name='Название')
    capacity = models.PositiveIntegerField(verbose_name='Макс. загрузка')

    def __str__(self):
        return '{}, {}'.format(self.title, self.capacity)

    def __unicode__(self):
        return '{}, {}'.format(self.title, self.capacity)


class Truck(models.Model):
    model = models.ForeignKey(TruckModel, verbose_name='Модель')
    number = models.PositiveIntegerField(verbose_name='Бортовой номер')
    current_load = models.PositiveIntegerField(
        default=0, verbose_name='Текущая загрузка'
    )
