from django.db import models

# Create your models here.
class ppleData(models.Model):
    Surname = models.CharField(blank=False, max_length=200)
    Firstname = models.CharField(blank=False, max_length=200)
    Email = models.EmailField(blank=False, max_length=200)
    Phone = models.IntegerField(blank=False)
    date_of_birth = models.CharField(blank=False, max_length=200)
    BVN = models.IntegerField(blank=False)
    address = models.CharField(max_length=150)
    guarantor_name = models.CharField(max_length=100)
    state_of_origin = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    school_degree = models.CharField(max_length=300)

    def __str__(self):
        return self.Surname


