from django.contrib import admin
from .models import Member

# Register your models here.
class memberAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','joined_date',)

admin.site.register(Member,memberAdmin)