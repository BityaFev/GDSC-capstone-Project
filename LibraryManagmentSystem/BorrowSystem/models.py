from django.db import models

from django.contrib.auth.models import User

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add = True)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)
