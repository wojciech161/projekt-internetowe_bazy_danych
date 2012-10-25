from LibraryServer.models import Author
from LibraryServer.models import User
from LibraryServer.models import Book
from LibraryServer.models import Borrow
from LibraryServer.models import Reservation
from LibraryServer.models import Publisher
from LibraryServer.models import Tome
from LibraryServer.models import Kind

class BorrowHelper:
	title = ""
	author = ""
	publisher = ""
	release = None
	kind = ""
	borrow_date = None
	borrow_id = 0

def get_borrows(uid):
	borrows = Borrow.objects.filter(user_id = uid)

	result = []

	for borrow in borrows:
		book = borrow.book_id
		tome = Tome.objects.get(book_id = book)
		author = tome.author_id
		publisher = tome.publisher_id
		kind = tome.kind

		helper = BorrowHelper()

		helper.title = tome.title
		helper.author = author.name_surname
		helper.publisher = publisher.name
		helper.release = tome.release_date
		helper.kind = kind.name
		helper.borrow_date = borrow.date_of_borrow
		helper.borrow_id = borrow.id

		result.append(helper)

	return result