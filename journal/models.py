# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#официальный дилер
class OfficialDealer(models.Model):
    name = models.CharField('Название', max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Дилер"
        verbose_name_plural = "Дилеры"

#детали, устанавливаемые в данную модель машины
class Detail(models.Model):
    name = models.CharField('Название', max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Деталь"
        verbose_name_plural = "Детали"

#модель машины
class CarModel(models.Model):
    name = models.CharField('Название', max_length=255)
    dealer = models.ForeignKey(OfficialDealer,verbose_name='Дилер')
    details = models.ManyToManyField(Detail,verbose_name='Детали')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

#машины
class Car(models.Model):
    name = models.CharField('Название', max_length=255)
    mileage = models.IntegerField('Пробег')
    model = models.ForeignKey(CarModel,verbose_name='Модель машины')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

#детали, установленные в машину
class CarDetail(models.Model):
    name = models.CharField('Название', max_length=255)
    mileage = models.IntegerField('Пробег')
    car = models.ForeignKey(Car,verbose_name='Машина')
    nomenclature = models.ForeignKey(Detail,verbose_name='Номенклатура детали')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Деталь"
        verbose_name_plural = "Детали"
