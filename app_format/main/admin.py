from django.contrib import admin
from .models import Trainer
from .models import Client
from .models import Training
from .models import Subscription

admin.site.register(Trainer)
admin.site.register(Client)
admin.site.register(Training)
admin.site.register(Subscription)

