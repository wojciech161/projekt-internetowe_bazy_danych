from LibraryServer.models import Author
from LibraryServer.models import User
from LibraryServer.models import Book
from LibraryServer.models import Borrow
from LibraryServer.models import Reservation
from LibraryServer.models import Publisher
from LibraryServer.models import Tome
from LibraryServer.models import Kind

class ReservationHelper:
	title = ""
	author = ""
	publisher = ""
	release = None
	kind = ""
	reservation_date = None
	reservation_id = 0
	reserver_name_surname = ""

def get_reservations(uid):
	reservations = Reservation.objects.filter(user_id = uid)

	result = []

	for reservation in reservations:
		book = reservation.book_id
		tome = Tome.objects.get(book_id = book)
		author = tome.author_id
		publisher = tome.publisher_id
		kind = tome.kind

		helper = ReservationHelper()

		helper.title = tome.title
		helper.author = author.name_surname
		helper.publisher = publisher.name
		helper.release = tome.release_date
		helper.kind = kind.name
		helper.reservation_date = reservation.date_of_reservation
		helper.reservation_id = reservation.id

		result.append(helper)

	return result

def get_all_reservations():
	reservations = Reservation.objects.all()

	result = []

	for reservation in reservations:
		book = reservation.book_id
		tome = Tome.objects.get(book_id = book)
		author = tome.author_id
		publisher = tome.publisher_id
		kind = tome.kind

		helper = ReservationHelper()

		helper.title = tome.title
		helper.author = author.name_surname
		helper.publisher = publisher.name
		helper.release = tome.release_date
		helper.kind = kind.name
		helper.reservation_date = reservation.date_of_reservation
		helper.reservation_id = reservation.id
		helper.reserver_name_surname = reservation.user_id.name + reservation.user_id.surname

		result.append(helper)

	return result