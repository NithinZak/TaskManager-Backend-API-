from django.contrib import admin
from .models import CustomUser,MdlTask

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(MdlTask)

