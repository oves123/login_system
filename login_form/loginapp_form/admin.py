from django.contrib import admin
from .models import user
# Register your models here.
admin.site.register(user)
class useradmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'password', 'confirm_password')
