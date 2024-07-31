from django.contrib import admin
from .models import Register, PostJob, Application

# Register your models here.
admin.site.register(Register)
admin.site.register(PostJob)
admin.site.register(Application)