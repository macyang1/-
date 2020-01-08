from django.contrib import admin
from api.models import *
# Register your models here.
admin.site.register(Food)
admin.site.register(FoodDetail)
admin.site.register(Category)
admin.site.register(Warehouse)

admin.site.register(SmallOrder)
admin.site.register(BigOrder)
admin.site.register(Active)

admin.site.register(Address)

