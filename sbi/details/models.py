from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=40)
    desc = models.TextField()
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
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
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
    CARD_CHOICES = (
        ('C', 'Credit Card'),
        ('D', 'Debit Card'),
    )
    card = models.CharField(max_length=1, choices=CARD_CHOICES)

    def __str__(self):
        return self.name


