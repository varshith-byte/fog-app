from django.contrib import admin

# Register your models here.
from fogapp.models import Profile, File_Save

admin.site.register(Profile)
admin.site.register(File_Save)
