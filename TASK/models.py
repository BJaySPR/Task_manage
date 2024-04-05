from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Task_Create(models.Model):
    title = models.CharField(max_length =200)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=20)
    assign_to = models.CharField(max_length =100)

    deadline = models.DateField(default = datetime.now() + timedelta(days=30))
    create_at = models.DateTimeField(auto_now_add=True, blank=False)

    update_at = models.DateTimeField(auto_now=True)
    
    


    def __str__(self):
        return self.title
    