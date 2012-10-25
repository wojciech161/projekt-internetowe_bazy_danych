from django.contrib import admin
from LibraryServer.models import Author
from LibraryServer.models import User
from LibraryServer.models import Book
from LibraryServer.models import Borrow
from LibraryServer.models import Reservation
from LibraryServer.models import Publisher
from LibraryServer.models import Tome
from LibraryServer.models import Kind

admin.site.register(Author)
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Reservation)
admin.site.register(Publisher)
admin.site.register(Tome)
admin.site.register(Kind)