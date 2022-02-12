from django.contrib import admin
from app.models import TODO
from .models import  Contact
# Register your models here.
admin.site.register(TODO)
admin.site.register(Contact)