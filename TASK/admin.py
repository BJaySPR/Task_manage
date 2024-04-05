from django.contrib import admin
from .models import Task_Create
# Register your models here.
@admin.register(Task_Create)
class Task_CreateAdmin(admin.ModelAdmin):
    list_display =['id','title','description','status','assign_to','deadline','create_at']

    