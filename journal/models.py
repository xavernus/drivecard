# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#машины
class Car(models.Model):
    name = models.CharField('Название', max_length=255)
    mileage = models.IntegerField('Пробег')

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

#детали, установленные в машину
class CarDetail(models.Model):
    name = models.CharField('Название', max_length=255)
    mileage = models.IntegerField('Пробег')

    class Meta:
        verbose_name = "Деталь"
        verbose_name_plural = "Детали"

#модель машины
class CarModel(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

#официальный дилер
class OfficialDealer(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = "Дилер"
        verbose_name_plural = "Дилеры"

#детали, устанавливаемые в данную модель машины
class Detail(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = "Деталь"
        verbose_name_plural = "Детали"
