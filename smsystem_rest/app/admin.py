from django.contrib import admin
from app.models import studentModel
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone']
    
    
admin.site.register(studentModel, studentAdmin)