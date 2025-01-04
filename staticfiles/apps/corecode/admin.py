from django.contrib import admin
from .models import SiteConfig, AcademicSession, AcademicTerm, Subject, StudentClass

@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    search_fields = ('key',)

@admin.register(AcademicSession)
class AcademicSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'current')
    list_filter = ('current',)
    search_fields = ('name',)

@admin.register(AcademicTerm)
class AcademicTermAdmin(admin.ModelAdmin):
    list_display = ('name', 'current')
    list_filter = ('current',)
    search_fields = ('name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

from .models import Profile,UserProfile

admin.site.register(Profile)
admin.site.register(UserProfile)



## signup fields data added..

# # admin.py
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# admin.site.register(User, UserAdmin)
