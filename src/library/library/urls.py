from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'LibraryServer.views.index', name='index'),
    url(r'^login/$', 'LibraryServer.views.login_page', name='login_page'),

    url(r'^librarian/(?P<user_id>\d+)/book_list/$', 'LibraryServer.views.librarian_book_list', name='librarian_book_list'),
    url(r'^librarian/(?P<user_id>\d+)/borrow/$', 'LibraryServer.views.librarian_borrow', name='librarian_borrow'),
    url(r'^librarian/(?P<user_id>\d+)/reservations_list/$', 'LibraryServer.views.librarian_reservations_list', name='librarian_reservations_list'),
    url(r'^librarian/(?P<user_id>\d+)/return/$', 'LibraryServer.views.librarian_return', name='librarian_return'),
    url(r'^librarian/(?P<user_id>\d+)/user_list/$', 'LibraryServer.views.librarian_user_list', name='librarian_user_list'),

    url(r'^user/(?P<user_id>\d+)/available_books/$', 'LibraryServer.views.user_available_books', name='user_available_books'),
    url(r'^user/(?P<user_id>\d+)/reservations/$', 'LibraryServer.views.user_reservations', name='user_reservations'),
)
