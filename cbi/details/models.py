from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=40)
    desc = models.TextField()
    wikipedia_url = models.URLField()
    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)


    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)


    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=10, choices= GENDER_CHOICES,default='male')
    mobile = models.CharField(max_length=12)
    email = models.EmailField()
    Address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)

    ACC_CHOICES = (
        ('S', 'Savings Account'),
        ('C', 'Current Account'),
    )
    account_f = models.CharField(max_length=1, choices=ACC_CHOICES)

    debit_card=models.BooleanField("Debit Card",default=False)
    credit_card = models.BooleanField("Credit Card", default=False)

    def __str__(self):
        return self.name


