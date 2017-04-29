from django.contrib import admin
from .models import item
from .models import itemcheck

admin.site.register(item)
admin.site.register(itemcheck)