from django.contrib import admin
from  .models import Profile,Comment,Images



# Register your models here.
admin.site.register(Profile)
admin.site.register(Images)
admin.site.register(Comment)
