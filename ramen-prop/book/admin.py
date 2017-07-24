from django.contrib import admin
from django_extensions.admin import ForeignKeyAutocompleteAdmin

from .models import Author
from .models import Book
from .models import BookMark
from .models import Comment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class AuthorAdmin(ForeignKeyAutocompleteAdmin):
    pass


@admin.register(BookMark)
class BookMarkAdmin(ForeignKeyAutocompleteAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(ForeignKeyAutocompleteAdmin):
    pass


