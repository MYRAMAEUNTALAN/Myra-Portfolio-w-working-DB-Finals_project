from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    phoneNumber = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.email
