from django.contrib import admin
from .models import Students, Schedule, Venue, Attendance, Batch

admin.site.register(Students)
admin.site.register(Schedule)
admin.site.register(Attendance)
admin.site.register(Venue)
admin.site.register(Batch)
