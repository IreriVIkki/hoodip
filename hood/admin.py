from __future__ import unicode_literals
from django.contrib import admin
from .models import *

# Register your models here.


class NeighborHoodAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_name',)


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(NeighborHood, NeighborHoodAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Business, BusinessAdmin)
