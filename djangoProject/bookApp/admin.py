from django.contrib import admin
from .models import Book, Author, Publication


class BookAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(BookAdmin, self).save_model(request, obj, form, change)

admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Publication)

# Register your models here.
