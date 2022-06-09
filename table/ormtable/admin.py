from django.contrib import admin

from .models import result, student,course

@admin.register(student)
class Admin(admin.ModelAdmin):
     list_display = ['first_name','last_name','details']

@admin.register(course)
class Admin(admin.ModelAdmin):
     list_display = ['course_id','course_name']

@admin.register(result)
class Admin(admin.ModelAdmin):
     list_display = ['result_id','result_grade']

# Register your models here.
