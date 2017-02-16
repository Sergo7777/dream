# -*- coding: utf-8 -*-
from django.db import models
from datetime import *


class Category(models.Model):
	name = models.CharField(max_length=255, verbose_name='Название категории')
	alias = models.SlugField(verbose_name='Alias категории')

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

	def __str__(self):
		return 'Категория %s' % self.name

# Create your models here.
class Product(models.Model):
	id = models.AutoField(primary_key=True)
	
	name = models.CharField(
		max_length=255, 
		verbose_name='Название товара')

	price = models.DecimalField(
		max_digits=10, 
		decimal_places=2,
		default=0, 
		verbose_name='Цена')

	image = models.ImageField(
		blank=True, 
		verbose_name='Фото',
		null=True)

	alias = models.SlugField(
		verbose_name='Alias товара')

	description = models.TextField(
		blank=True,
		verbose_name="Описание товара")

	created = models.DateTimeField(auto_now_add=True)

	updated = models.DateTimeField(auto_now=True)

	category = models.ForeignKey(Category)

	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товары"

	def __str__(self):
		return 'Товар %s' % self.name

