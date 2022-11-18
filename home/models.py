from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    hosting = models.BooleanField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name