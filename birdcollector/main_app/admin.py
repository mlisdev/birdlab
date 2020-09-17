from django.contrib import admin
# add Feeding to the import
from .models import Bird, Feeding

admin.site.register(Bird)
# register the new Feeding Model 
admin.site.register(Feeding)