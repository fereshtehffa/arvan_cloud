from django.contrib import admin
from .models import NameException, Bucket
# Register your models here.

admin.site.register(Bucket)
admin.site.register(NameException)