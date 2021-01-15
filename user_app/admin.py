from django.contrib import admin
from .models import User, Producer, Consumer

admin.site.register(User)
admin.site.register(Producer)
admin.site.register(Consumer)
