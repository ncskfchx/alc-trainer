from django.contrib import admin
from .models import TestModel, ProgressModel


admin.site.register(TestModel)
admin.site.register(ProgressModel)
