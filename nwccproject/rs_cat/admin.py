from django.contrib import admin

# Register your models here.

from .models import Rs_Cat,GroupActPrb
from django import forms

#class Rs_Cat_personal_form(forms.ModelForm):
    # add a field to select a car
#    GroupActPrb = forms.ModelMultipleChoiceField(GroupActPrb.objects.all())

class Rs_CatAdmin(admin.ModelAdmin):
    fieldsets = [
        ('แหล่งชุดข้อมูล',{'fields': ['name','link','GroupActPrb']}),
        ('หมายเหตุกำกับโดย ผู้กรอก',{'fields':['note','keyword','status']}),
        ('รายละเอียดประกอบ',{'fields': ['description','agency','agency_provided_data',
    'Time_period','source','type_of_data','date_recived','reference_doc','document01','document02','document03','related_subject',
    'data_licensing']}),
    ]
    search_fields = ('name', 'keyword', 'description', )
    list_display = ('name', 'GroupActPrb','status')
    list_filter = ('GroupActPrb','status')
    list_per_page = 50 
    
#    form = Rs_Cat_personal_form
    
admin.site.register(Rs_Cat, Rs_CatAdmin)

class GroupActPrbAdmin(admin.ModelAdmin):
    fieldsets = [
        ('กลุ่มข้อมูล ตามแผนแม่บท และพรบ.ทรัพยากรน้ำพ.ศ.2561',{'fields': ['NumOrder','name','description']}),
    ]
admin.site.register(GroupActPrb, GroupActPrbAdmin)