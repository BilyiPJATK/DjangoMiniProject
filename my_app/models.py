from django.db import models



# Create your models here.

class ContactFormSubmission(models.Model):
    email = models.EmailField(unique=True, max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.email