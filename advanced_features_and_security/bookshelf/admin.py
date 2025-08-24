from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # استورد الـ CustomUser من models.py

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "date_of_birth", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

# سجل CustomUser مع الـ Admin
admin.site.register(CustomUser, CustomUserAdmin)