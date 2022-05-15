from re import M
from django.db import models
# Create your models here.


class Donator(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=45)
    photo = models.TextField()
    password = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return self.name


class Donee(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=45)
    photo = models.TextField()
    description = models.CharField(max_length=255)
    password = models.CharField(max_length=100, null=False)
    
    def __str__(self) -> str:
        return self.name


class Child(models.Model):
    name = models.CharField(max_length=100)
    photo = models.TextField()
    description = models.CharField(max_length=255)
    subscription_cost = models.IntegerField()
    donee_id = models.ForeignKey(Donee, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    child_id = models.ForeignKey(Child, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title


class Subscription(models.Model):
    donator_id = models.ForeignKey(Donee, on_delete=models.CASCADE)
    child_id = models.ForeignKey(Child, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return self.donator_id.name + " - " + self.child_id.name