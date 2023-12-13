from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(StudentGroup),
admin.site.register(Course),
admin.site.register(Seminar),
admin.site.register(Notification),
admin.site.register(BestStudent),
admin.site.register(Profile),
admin.site.register(Lecturer),
admin.site.register(AdministrativeStaff),
admin.site.register(Technical)