from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import CustomUser ,  CustomUserAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # دي الكلاس اللي انت عاملها في models.py

admin.site.register(CustomUser, CustomUserAdmin)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "date_of_birth", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
