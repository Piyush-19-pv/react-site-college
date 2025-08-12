from django.db import models

# Create your models here.
from django.db import models
from django.db import models
from django.utils.timezone import now
# models.py

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.rating} Stars)"





class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class VisitorLog(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    timestamp = models.DateTimeField(default=now)
    cookies_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ip_address} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"




COURSE_CHOICES = [
    ('BCA', 'BCA'),
    ('MCA', 'MCA'),
    ('B.Com', 'B.Com'),
    ('M.Com', 'M.Com'),
    ('BBA', 'BBA'),
    ('MBA', 'MBA'),
    ('B.Sc', 'B.Sc'),
    ('M.Sc', 'M.Sc'),
    ('BBA LL.B', 'BBA LL.B'),
    ('BA LL.B', 'BA LL.B'),
    ('LL.B', 'LL.B'),
]

class Application(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    course = models.CharField(max_length=20, choices=COURSE_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.course}"