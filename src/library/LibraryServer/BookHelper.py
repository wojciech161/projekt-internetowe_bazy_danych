from LibraryServer.models import Author
from LibraryServer.models import User
from LibraryServer.models import Book
from LibraryServer.models import Borrow
from LibraryServer.models import Reservation
from LibraryServer.models import Publisher
from LibraryServer.models import Tome
from LibraryServer.models import Kind

class BookHelper:
	book_id = ""
	title = ""
	author = ""
	publisher = ""
	release = None
	kind = ""
	amount = 0
	availability = 0

def get_books():
	result = []

	books = Book.objects.all()

	for book in books:
		tome = Tome.objects.get(book_id = book)
		author = tome.author_id
		publisher = tome.publisher_id
		kind = tome.kind

		new_book = BookHelper()
		new_book.book_id = book.id
		new_book.title = tome.title
		new_book.author = author.name_surname
		new_book.publisher = publisher.name
		new_book.release = tome.release_date
		new_book.kind = kind.name
		new_book.amount = tome.amount
		new_book.availability = book.availability

		result.append(new_book)

	return result
