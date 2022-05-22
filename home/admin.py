from django.contrib import admin
from .models import Region, District, Student, Course
# Register your models here.
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Student)
admin.site.register(Course)