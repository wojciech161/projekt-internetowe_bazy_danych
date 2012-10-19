#-*- coding: utf-8 -*-
from django.db import models

class Users(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=50)
	address = models.CharField(max_length=70)
	date_of_birth = models.DateTimeField('Data urodzenia')
	pesel = models.IntegerField()
	user_type = models.IntegerField()
	user_active = models.IntegerField()

class Authors(models.Model):
	name_surname = models.CharField(max_length=70)

class Books(models.Model):
	availability = models.IntegerField()

class Borrows(models.Model):
	book_id = models.ForeignKey(Books)
	user_id = models.ForeignKey(Users)
	date_of_borrow = models.DateTimeField('Data wypożyczenia')

class Reservations(models.Model):
	book_id = models.ForeignKey(Books)
	user_id = models.ForeignKey(Users)
	date_of_reservation = models.DateTimeField('Data rezerwacji')

class Publishers(models.Model):
	name = models.CharField(max_length=50)

class Tomes(models.Model):
	author_id = models.ForeignKey(Authors)
	publisher_id = models.ForeignKey(Publishers)
	book_id = models.ForeignKey(Books)
	kind = (
		('Drama', 'Dramat'),
		('Scientific', 'Nauka'),
		('Kids', 'Dla dzieci'),
		('Poetry', 'Poezja'),
		('School', 'Podręcznik'),
		('Novel', 'Nowela'),
	)
	title = models.CharField(max_length=255)
	release_date = models.DateTimeField('Data wydania')
	amount = models.IntegerField()
