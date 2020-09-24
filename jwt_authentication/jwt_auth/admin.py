from django.contrib import admin
from . import models as auth

# Register your models here.

admin.site.register(auth.Role)
admin.site.register(auth.UserPermissions)
admin.site.register(auth.UserInfo)


