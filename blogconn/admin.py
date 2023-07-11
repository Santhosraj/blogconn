from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile,Uploads,Room,Message,Comment

# Register your models here.
admin.site.register(Profile)

admin.site.register(Uploads)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Comment)