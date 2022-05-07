from django.contrib import admin
from app1.models import User
# Register your models here.

class Useradmin(admin.ModelAdmin):
    list_display = ['is_rmanager','is_omanager','is_customer']
admin.site.register(User)