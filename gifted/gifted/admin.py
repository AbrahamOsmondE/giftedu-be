from django.contrib import admin

from .models import Donator,Donee,Child,Post,Subscription

admin.site.register(Donator)
admin.site.register(Donee)
admin.site.register(Child)
admin.site.register(Post)
admin.site.register(Subscription)