#-*- coding: utf-8 -*-
from django.db import models

class User(models.Model):
	login = models.CharField(max_length=50)
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=50)
	address = models.CharField(max_length=70)
	date_of_birth = models.DateField('Data urodzenia')
	pesel = models.IntegerField()
	user_type = models.IntegerField()
	user_active = models.IntegerField()

class Author(models.Model):
	name_surname = models.CharField(max_length=70)

class Book(models.Model):
	availability = models.IntegerField()

class Borrow(models.Model):
	book_id = models.ForeignKey(Book)
	user_id = models.ForeignKey(User)
	date_of_borrow = models.DateField('Data wypożyczenia')

class Reservation(models.Model):
	book_id = models.ForeignKey(Book)
	user_id = models.ForeignKey(User)
	date_of_reservation = models.DateField('Data rezerwacji')

class Publisher(models.Model):
	name = models.CharField(max_length=50)

class Kind(models.Model):
	name = models.CharField(max_length=50)

class Tome(models.Model):
	author_id = models.ForeignKey(Author)
	publisher_id = models.ForeignKey(Publisher)
	book_id = models.ForeignKey(Book)
	kind = models.ForeignKey(Kind)
	title = models.CharField(max_length=255)
	release_date = models.DateField('Data wydania')
	amount = models.IntegerField()
