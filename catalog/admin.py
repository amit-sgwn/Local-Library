from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author,AuthorAdmin)
#admin.site.register(Genre)
#admin.site.register(BookInstance)
