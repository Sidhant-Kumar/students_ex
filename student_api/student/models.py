from django.db import models


class students(models.Model):
    first = models.CharField(max_length=70, blank=False, default='')
    last = models.CharField(max_length=70, default='')
    email_id = models.EmailField(max_length=250)
    phone = models.IntegerField(max_length=10)
