from django.contrib import admin
from  .models import Profiles,Comment,Images



# Register your models here.
admin.site.register(Profiles)
admin.site.register(Images)
admin.site.register(Comment)
