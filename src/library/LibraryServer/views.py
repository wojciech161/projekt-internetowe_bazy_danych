from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from LibraryServer.models import Authors
from LibraryServer.models import Users
from LibraryServer.models import Books
from LibraryServer.models import Borrows
from LibraryServer.models import Reservations
from LibraryServer.models import Publishers
from LibraryServer.models import Tomes

#Main pages

def index(request):
	return render(request, 'views/index.html')

def login_page(request):

	if request.POST:
		username = request.POST.get('login')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password)

		if user is not None:
			loggedUser = Users.objects.get(login=username)
			if loggedUser.user_active == 1:
				login(request, user)
				if loggedUser.user_type == 1:
					return HttpResponseRedirect(reverse('LibraryServer.views.librarian_user_list', args=(loggedUser.id,)))
				if loggedUser.user_type == 2:
					return HttpResponseRedirect(reverse('LibraryServer.views.user_available_books', args=(loggedUser.id,)))

	return render(request, 'views/login_page.html')


#Librarian main pages

def librarian_user_list(request, user_id):
	return render(request, 'views/librarian_user_list.html', {'user_id':user_id})

def librarian_book_list(request, user_id):
	return render(request, 'views/librarian_book_list.html', {'user_id':user_id})

def librarian_borrow(request, user_id):
	return render(request, 'views/librarian_borrow.html', {'user_id':user_id})

def librarian_return(request, user_id):
	return render(request, 'views/librarian_return.html', {'user_id':user_id})

def librarian_reservations_list(request, user_id):
	return render(request, 'views/librarian_reservations_list.html', {'user_id':user_id})

#Librarian additional pages

def librarian_add_user(request, user_id):
	return HttpResponse("Dodaj uzytkownika")

def librarian_modify_user(request, user_id, modified_user_id):
	return HttpResponse("Modyfikuj uzytkownika %s", modified_user_id)

def librarian_browse_user_card(request, user_id, usercard_id):
	return HttpResponse("Przegladaj karte uzytkownika %s", usercard_id)

def librarian_deactivate_user(request, user_id, deactivated_user_id):
	return HttpResponse("Dezaktywuj uzytkownika %s", deactivated_user_id)

def librarian_borrow_select_user(request, user_id, book_id):
	return HttpResponse("Wybierz uzytkownika co mu sie wypozycza ksiazke %s", book_id)


#User Main Pages

def user_available_books(request, user_id):
	return render(request, 'views/user_available_books.html', {'user_id':user_id})

def user_reservations(request, user_id):
	return render(request, 'views/user_reservations.html', {'user_id':user_id})

def user_borrows(request, user_id):
	return render(request, 'views/user_borrows.html', {'user_id':user_id})
