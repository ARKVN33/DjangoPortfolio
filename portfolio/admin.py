from django.contrib import admin
from .models import Skill


# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'percent')
    list_filter = ('title', 'percent')
    search_fields = ('title', 'percent')


admin.site.register(Skill, SkillAdmin)
