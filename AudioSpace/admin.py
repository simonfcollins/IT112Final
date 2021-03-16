from django.contrib import admin
from .models import Review, Discussion, Forum

admin.site.register(Discussion)
admin.site.register(Forum)
admin.site.register(Review)
# Register your models here.
