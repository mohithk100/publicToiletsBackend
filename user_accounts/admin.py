from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class customUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None , {'fields':('mobileNumber','avatar')}),
    )

admin.site.register(User , customUserAdmin)
