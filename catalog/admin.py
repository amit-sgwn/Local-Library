from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(BookInstance)
