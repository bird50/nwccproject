from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
#หน่วยงานระดับกรม
class Agency(models.Model):
    class Meta :
#        ordering=('ministry',)
        verbose_name='หน่วยงานระดับกรม'
        verbose_name_plural='หน่วยงานระดับกรม'
    
    small_name = models.CharField(
        max_length=55,
        null=True,
        verbose_name='ชื่อย่อ (หน่วยงานระดับกรม)',
    )
    department = models.TextField(null=False,verbose_name='ชื่อหน่วยงาน ระดับกรม')
    establish = models.CharField(max_length=4,null=True,verbose_name='จัดตั้งเมื่อ (พ.ศ.)',)
    #ministry = models.TextField(null=True,verbose_name='ชื่อหน่วยงาน ระดับกระทรวง')
    ministry = models.ForeignKey('Ministry',related_name='Ministry',blank=True,null=True,on_delete=models.SET_NULL,verbose_name='สังกัดกระทรวง')
    def __str__(self):
        return self.department
        
class Ministry(models.Model):
    class Meta :
#        ordering=('ministry',)
        verbose_name='หน่วยงานระดับกระดับกระทรวง'
        verbose_name_plural='หน่วยงานระดับกระทรวง'
    small_name = models.CharField(max_length=55,null=True,verbose_name='ชื่อย่อ (หน่วยงานระดับกระทรวง)',)
    ministry = models.TextField(null=False,verbose_name='ชื่อหน่วยงาน ระดับกระทรวง')
    establish = models.CharField(max_length=4,null=True,verbose_name='จัดตั้งเมื่อ (พ.ศ.)',)
    def __str__(self):
        return self.ministry
