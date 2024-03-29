# Generated by Django 3.1.1 on 2021-07-17 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_birth', models.DateField()),
                ('active_is', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('clients', models.ManyToManyField(to='main.Client')),
                ('trainer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_count', models.IntegerField(default=10)),
                ('price', models.IntegerField()),
                ('date_start', models.DateField()),
                ('month_count', models.IntegerField(default=1)),
                ('type', models.CharField(max_length=5)),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.client')),
            ],
        ),
    ]
