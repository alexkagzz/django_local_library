from django.contrib import admin

# Register your models here.
from catalog.models import Book, Author, Language, Genre, BookInstance

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)


#  Add Inline editing of associated records
class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book

#  Add Inline editing of associated records
class BooksInstanceInline(admin.TabularInline):
    """Defines format of inline book instance insertion (used in BookAdmin)"""
    model = BookInstance


# Define the admin class to castomize display
class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.
       Defines:
        - fields to be displayed in list view (list_display)
        - orders fields in detail view (fields),
          grouping the date fields horizontally
        - adds inline addition of books in author view (inlines)
       """
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # Controlling which fields are displayed and laid out
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Administration object for Book models.
       Defines:
        - fields to be displayed in list view (list_display)
        - adds inline addition of book instances in book view (inlines)
       """
    list_display = ('title', 'author', 'display_genre')
    #  Add Inline editing of associated records
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Administration object for BookInstance models.
      Defines:
       - fields to be displayed in list view (list_display)
       - filters that will be displayed in sidebar (list_filter)
       - grouping of fields into sections (fieldsets)
      """
    list_display = ('book', 'status', 'due_back')
    # Introduce a filter
    list_filter = ('status', 'due_back')
    # Sectioning the detail view
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
