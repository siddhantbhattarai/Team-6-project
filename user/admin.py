from django.contrib import admin
from django.contrib.auth.models import User, Group
from . models import Profile
# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    list_display_links = ['username', 'email']
    #list_editable = ['is_active', 'is_staff', 'is_superuser']
    inlines = [ProfileInline]
    

admin.site.register(User,UserAdmin)

#mixing profile info into user info

