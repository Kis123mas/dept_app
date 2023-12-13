from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib.admin import AdminSite, AdminSiteMixin
from django.contrib import admin

class CustomAdminSite(AdminSite, AdminSiteMixin):
    index_template = 'admin_custom_index.html'

custom_admin_site = CustomAdminSite(name='customadmin')

admin.site.register(StudentGroup),
admin.site.register(Course),
admin.site.register(Seminar),
admin.site.register(Notification),
admin.site.register(BestStudent),
admin.site.register(Profile),
admin.site.register(Lecturer),
admin.site.register(AdministrativeStaff),
admin.site.register(Technical)