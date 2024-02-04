from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Student)

class Student_admin(admin.ModelAdmin):
    list_display=[field.name for field in Student._meta.fields]
