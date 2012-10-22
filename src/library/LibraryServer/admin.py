from django.contrib import admin
from LibraryServer.models import Authors
from LibraryServer.models import Users
from LibraryServer.models import Books
from LibraryServer.models import Borrows
from LibraryServer.models import Reservations
from LibraryServer.models import Publishers
from LibraryServer.models import Tomes

admin.site.register(Authors)
admin.site.register(Users)
admin.site.register(Books)
admin.site.register(Borrows)
admin.site.register(Reservations)
admin.site.register(Publishers)
admin.site.register(Tomes)