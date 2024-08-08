from django.contrib import admin

from to_do_app import models

# Register your models here.
admin.site.register(models.Test)
admin.site.register(models.Todo)