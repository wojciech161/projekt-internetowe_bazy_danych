from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout, models
from django.core.urlresolvers import reverse
from LibraryServer.models import Author
from LibraryServer.models import User
from LibraryServer.models import Book
from LibraryServer.models import Borrow
from LibraryServer.models import Reservation
from LibraryServer.models import Publisher
from LibraryServer.models import Tome
from LibraryServer.models import Kind
from BookHelper import BookHelper, get_books
from datetime import date
from ReservationHelper import ReservationHelper, get_reservations, get_all_reservations
from BorrowHelper import BorrowHelper, get_borrows, get_all_borrows
from UserHelper import UserHelper, get_all_readers

#Main pages

def index(request):
	return render(request, 'views/index.html')

def login_page(request):

	if request.POST:
		username = request.POST.get('login')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password)

		if user is not None:
			loggedUser = User.objects.get(login=username)
			if loggedUser.user_active == 1:
				login(request, user)
				if loggedUser.user_type == 1:
					return HttpResponseRedirect(reverse('LibraryServer.views.librarian_user_list', args=(loggedUser.id,)))
				if loggedUser.user_type == 2:
					return HttpResponseRedirect(reverse('LibraryServer.views.user_available_books', args=(loggedUser.id,)))

	return render(request, 'views/login_page.html')

def service_logout(request):
	logout(request)
	return render(request, 'views/index.html')


#Librarian main pages

def librarian_user_list(request, user_id):
	if request.user.is_authenticated():

		user_list = get_all_readers()

		return render(request, 'views/librarian_user_list.html', {'user_id':user_id, 'users':user_list})
	else:
		return render(request, 'views/index.html')

def librarian_book_list(request, user_id):
	if request.user.is_authenticated():

		book_list = get_books()

		return render(request, 'views/librarian_book_list.html', {'user_id':user_id, 'books':book_list})
	else:
		return render(request, 'views/index.html')

def librarian_borrow(request, user_id):
	if request.user.is_authenticated():

		book_list = get_books()

		return render(request, 'views/librarian_borrow.html', {'user_id':user_id, 'books':book_list})
	else:
		return render(request, 'views/index.html')

def librarian_return(request, user_id):
	if request.user.is_authenticated():

		borrows = get_all_borrows()

		return render(request, 'views/librarian_return.html', {'user_id':user_id, 'borrows':borrows})
	else:
		return render(request, 'views/index.html')

def librarian_reservations_list(request, user_id):
	if request.user.is_authenticated():

		reservations = get_all_reservations()

		return render(request, 'views/librarian_reservations_list.html', {'user_id':user_id, 'reservations':reservations})
	else:
		return render(request, 'views/index.html')

#Librarian additional pages

def librarian_add_user(request, user_id):
	if request.user.is_authenticated():

		if request.POST:
			user = User()
			user.login = request.POST.get('edit_login')
			user.name = request.POST.get('edit_name')
			user.surname = request.POST.get('edit_surname')
			user.address = request.POST.get('edit_address')
			user.date_of_birth = request.POST.get('edit_date_of_birth')
			user.pesel = request.POST.get('edit_pesel')
			user.user_type = 2
			user.user_active = 1
			password = request.POST.get('edit_password')

			user.save()

			usr = models.User.objects.create_user(user.login, 'user@biblioteka.pl', password)
			usr.is_staff = False
			usr.save()

			user_list = get_all_readers()

			return render(request, 'views/librarian_user_list.html', {'user_id':user_id, 'users':user_list})

		return render(request, 'views/librarian_add_user.html', {'user_id':user_id})
	else:
		return render(request, 'views/index.html')

def librarian_modify_user(request, user_id, modified_user_id):
	if request.user.is_authenticated():
		return HttpResponse("Modyfikuj uzytkownika")
	else:
		return render(request, 'views/index.html')

def librarian_browse_user_card(request, user_id, usercard_id):
	if request.user.is_authenticated():
		return HttpResponse("Przegladaj karte uzytkownika")
	else:
		return render(request, 'views/index.html')

def librarian_deactivate_user(request, user_id, deactivated_user_id):
	if request.user.is_authenticated():
		user = User.objects.get(id = deactivated_user_id)
		user.user_active = 0
		user.save()
		user_list = get_all_readers()

		return render(request, 'views/librarian_user_list.html', {'user_id':user_id, 'users':user_list})
	else:
		return render(request, 'views/index.html')

def librarian_borrow_select_user(request, user_id, book_id):
	if request.user.is_authenticated():
		users = get_all_readers()
		return render(request, 'views/librarian_borrow_select_user.html', {'user_id':user_id, 'users':users, 'book_id':book_id})
	else:
		return render(request, 'views/index.html')

def librarian_borrow_book_return_borrows(request, user_id, book_id, borrower_id):
	if request.user.is_authenticated():
		borrow = Borrow()
		borrow.book_id = Book.objects.get(id = book_id)
		borrow.user_id = User.objects.get(id = borrower_id)
		borrow.date_of_borrow = date.today()

		borrow.save()

		tome = Tome.objects.get(book_id = borrow.book_id)
		tome.amount = tome.amount - 1
		tome.save()

		if tome.amount == 0:
			borrow.book_id.availability = 0
			borrow.book_id.save()

		book_list = get_books()

		return render(request, 'views/librarian_borrow.html', {'user_id':user_id, 'books':book_list})

	else:
		return render(request, 'views/index.html')

def librarian_borrow_book_return_reservations(request, user_id, reservation_id):
	if request.user.is_authenticated():
		
		reservation = Reservation.objects.get(id = reservation_id)

		borrow = Borrow()
		borrow.book_id = reservation.book_id
		borrow.user_id = reservation.user_id
		borrow.date_of_borrow = date.today()

		borrow.save()

		reservation.delete()

		reservations = get_all_reservations()

		return render(request, 'views/librarian_reservations_list.html', {'user_id':user_id, 'reservations':reservations})
	else:
		return render(request, 'views/index.html')

def librarian_return_book(request, user_id, borrow_id):
	if request.user.is_authenticated():
		
		borrow = Borrow.objects.get(id = borrow_id)
		book = borrow.book_id
		tome = Tome.objects.get(book_id = book)

		tome.amount = tome.amount + 1
		if book.availability == 0:
			book.availability = 1
			book.save()

		tome.save()

		borrow.delete()

		borrows = get_all_borrows()

		return render(request, 'views/librarian_return.html', {'user_id':user_id, 'borrows':borrows})

	else:
		return render(request, 'views/index.html')

def librarian_delete_reservation(request, user_id, reservation_id):
	if request.user.is_authenticated():
		
		reservation = Reservation.objects.get(id = reservation_id)
		book = reservation.book_id
		tome = Tome.objects.get(book_id = book)

		tome.amount = tome.amount + 1
		if book.availability == 0:
			book.availability = 1
			book.save()

		tome.save()

		reservation.delete()

		reservations = get_all_reservations()

		return render(request, 'views/librarian_reservations_list.html', {'user_id':user_id, 'reservations':reservations})

	else:
		return render(request, 'views/index.html')


#User Main Pages

def user_available_books(request, user_id):
	if request.user.is_authenticated():
		book_list = get_books()
		return render(request, 'views/user_available_books.html', {'user_id':user_id, 'books': book_list})
	else:
		return render(request, 'views/index.html')

def user_reservations(request, user_id):
	if request.user.is_authenticated():

		reservations = get_reservations(user_id)

		return render(request, 'views/user_reservations.html', {'user_id':user_id, 'reservations':reservations})
	else:
		return render(request, 'views/index.html')

def user_borrows(request, user_id):
	if request.user.is_authenticated():

		borrows = get_borrows(user_id)

		return render(request, 'views/user_borrows.html', {'user_id':user_id, 'borrows':borrows})
	else:
		return render(request, 'views/index.html')

#User additional pages

def user_reserve(request, user_id, book_id):
	if request.user.is_authenticated():

		reservation = Reservation()
		book = Book.objects.get(id = book_id)
		user = User.objects.get(id = user_id)
		reservation.book_id = book
		reservation.user_id = user
		reservation.date_of_reservation = date.today()

		reservation.save()

		tomes = Tome.objects.get(book_id = book)
		tomes.amount = tomes.amount - 1
		if tomes.amount == 0:
			book.availability = 0
			book.save()

		tomes.save()

		book_list = get_books()

		return render(request, 'views/user_available_books.html', {'user_id':user_id, 'books': book_list})

	else:
		return render(request, 'views/index.html')

def user_reserve_delete(request, user_id, reservation_id):
	if request.user.is_authenticated():
		reservation = Reservation.objects.get(id = reservation_id)
		book = reservation.book_id
		tome = Tome.objects.get(book_id = book)

		tome.amount = tome.amount + 1
		if book.availability == 0:
			book.availability = 1
			book.save()

		tome.save()

		reservation.delete()

		reservations = get_reservations(user_id)
		return render(request, 'views/user_reservations.html', {'user_id':user_id, 'reservations':reservations})

	else:
		return render(request, 'views/index.html')



