from LibraryServer.models import Author
from LibraryServer.models import User
from LibraryServer.models import Book
from LibraryServer.models import Borrow
from LibraryServer.models import Reservation
from LibraryServer.models import Publisher
from LibraryServer.models import Tome
from LibraryServer.models import Kind

class UserHelper:
	name = ""
	surname = ""
	address = ""
	birth_date = None
	pesel = 0
	active = 0
	user_id = 0

def get_all_readers():

	users = User.objects.filter(user_type = 2)

	result = []

	for user in users:
		user_helper = UserHelper()
		user_helper.name = user.name
		user_helper.surname = user.surname
		user_helper.address = user.address
		user_helper.birth_date = user.date_of_birth
		user_helper.pesel = user.pesel
		user_helper.active = user.user_active
		user_helper.user_id = user.id

		result.append(user_helper)

	return result