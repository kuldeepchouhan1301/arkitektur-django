from django.contrib import admin

# Register your models here.

from .models import Service, Project, Testimonial

admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Testimonial)