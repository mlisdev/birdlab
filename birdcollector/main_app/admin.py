from django.contrib import admin
# add Feeding to the import
from .models import Bird, Feeding, Toy

admin.site.register(Bird)
admin.site.register(Feeding)
admin.site.register(Toy)