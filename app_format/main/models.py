from django.db import models


class Trainer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)


class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    date_birth = models.DateField()
    active = models.BooleanField()


class Subscription(models.Model):
    id = models.IntegerField(primary_key=True)
    training_count = models.IntegerField(default=10)
    price = models.IntegerField()
    date_start = models.DateField()
    month_count = models.IntegerField(default=1)
    client_id = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=5)


class Training(models.Model):
    id = models.IntegerField(primary_key=True)
    date_time = models.DateTimeField()
    trainer_id = models.ForeignKey('Trainer', on_delete=models.SET_NULL, null=True)  # set restrict or set_null?????
    clients = models.ManyToManyField(Client)

