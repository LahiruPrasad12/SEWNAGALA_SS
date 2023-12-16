from django.contrib import admin

# Register your models here.
from .models import Student, Sibling, Achievement, Role

class SiblingInline(admin.TabularInline):
    model = Sibling
    extra = 1

class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 1
    classes = ['collapse']

class StudentAdmin(admin.ModelAdmin):
    inlines = [SiblingInline, AchievementInline]
    list_display = ('full_name', 'have_siblings')

admin.site.register(Student, StudentAdmin)