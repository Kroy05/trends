from django.contrib import admin
from .models import contacts


class contact_admin(admin.ModelAdmin):
    list_display=("name","number","mail","subject","message")

admin.site.register(contacts,contact_admin)

# Register your models here.
