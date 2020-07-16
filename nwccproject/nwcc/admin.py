from django.contrib import admin

# Register your models here.
from .models import Agency,Ministry

class AgencyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('หน่วยงาน',{'fields': ['department','ministry','small_name','establish']}),
    ]
admin.site.register(Agency, AgencyAdmin)

class MinistryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('หน่วยงาน',{'fields': ['ministry','small_name','establish']}),
    ]
admin.site.register(Ministry, MinistryAdmin)

