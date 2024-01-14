from django.contrib import admin
from .models import Book, Author, Genre, BookInstance


admin.site.register(Genre)


class BookAdmin(admin.TabularInline):
    model = Book
    exclude = ['summary', 'genre']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', "date_of_birth", 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookAdmin]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('imprint', 'book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = ((None, {'fields': ('book', 'imprint', 'id')}), ('Availability', {'fields': ('status', 'due_back')}),)
