from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'views/index.html')

def login_page(request):
	return HttpResponse("Login page")

def librarian_book_list(request, user_id):
	print user_id
	return HttpResponse("librarian book list")

def librarian_borrow(request, user_id):
	return HttpResponse("librarian borrow")

def librarian_reservations_list(request, user_id):
	return HttpResponse("Librarian reservations list")

def librarian_return(request, user_id):
	return HttpResponse("Librarian return")

def librarian_user_list(request, user_id):
	return HttpResponse("Librarian user list")

def user_available_books(request, user_id):
	return HttpResponse("User available books")

def user_reservations(request, user_id):
	return HttpResponse("User reservations")

