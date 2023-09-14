from django.db import models

# Create your models here.
class RegistrationDetail(models.Model):
    type_of_reg = models.CharField(max_length=100)
    completed = models.IntegerField()
    ongoing = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.type_of_reg