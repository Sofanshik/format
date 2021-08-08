from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=30)
    date_birth = models.DateField()
    active = models.BooleanField()

    def __str__(self):
        return self.name


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
