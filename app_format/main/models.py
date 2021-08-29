from django.db import models
from django.urls import reverse


class Trainer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, default="")
    email = models.EmailField(max_length=254, default="")
    date_birth = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('definite_client_url', kwargs={'client_id': self.pk})


class Subscription(models.Model):
    training_count = models.IntegerField(default=10)
    price = models.IntegerField()
    date_start = models.DateField()
    month_count = models.IntegerField(default=1)
    client_id = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=5)

    def __str__(self):
        return self.type


class Training(models.Model):
    date_time = models.DateTimeField()
    trainer_id = models.ForeignKey('Trainer', on_delete=models.SET_NULL, null=True)  # set restrict or set_null?????
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return self.date_time
