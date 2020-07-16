from django.db import models
from multiselectfield import MultiSelectField

from django.utils.translation import gettext_lazy as _
# Create your models here.

class Rs_Cat(models.Model):
    class Meta :
        verbose_name='ชุดข้อมูล'
        verbose_name_plural='ชุดข้อมูล'
    Type_of_data=[
        ('CSV', _('CSV')),
        ('TXT', _('Text file')),
        ('XLS', _('Excel file,xlsx,xls,xl*')),
        ('SHP', _('ESRI Shape file')),
        ('ETC', _('Other formats')),
        ('UNK', _('Unknown format')),
    ]
    GroupActPrb_dict = [
        ('G-01','1) การจัดการน้ำ เพื่ออุปโภคบริโภค'),
        ('G-02','2) การจัดการน้ำ เพื่อการเกษตร/ประมง'),
        ('G-03','3) การจัดการน้ำ เพื่ออุตสาหกรรม'),
        ('G-04','4) การเตือนภัยและจัดการสถานการณ์น้ำท่วม'),
        ('G-05','5) การเตือนภัยและจัดการสถานการณ์ภัยแล้ง'),
        ('G-06','6) การจัดการคุณภาพน้ำและรักษาระบบนิเวศและอนุรักษ์ทรัพยากรน้ำสาธารณะ'),
        ('G-07','7) การอนุรักษ์ฟื้นฟูสภาพป่าต้นน้ำที่เสื่อมโทรมและป้องกันการพังทลายของดิน'),
        ('G-08','8) การจัดการแผนงานโครงการด้านทรัพยากรน้ำ'),
        ('G-09','9) การจัดการและส่งเสริมนวัตกรรมด้านทรัพยากรน้ำ'),
        ('G-10','10) การบริหารจัดการน้ำ'),
        ('G-11','11) การอนุญาตใช้น้ำ'),
        ('G-12','12) การจัดการผังน้ำ'),
    ]
    status_dict = [
        ('00','รับข้อมูล'),
        ('01','อยู่ระหว่างตรวจสอบ'),
        ('09','ข้อมูลพร้อม!!!')
    ]
    name = models.CharField(max_length=255,verbose_name='ชื่อชุดข้อมูล')
    link = models.URLField(blank=True,verbose_name='ลิ๊งค์ที่อยู่ข้อมูล')
    agency = models.ForeignKey('nwcc.Agency',related_name='Agency', blank=True, null=True,on_delete=models.SET_NULL,verbose_name='ชื่อหน่วยงานเจ้าของ/รับผิดชอบข้อมูล (ระดับกรม)')
    agency_provided_data = models.ForeignKey('nwcc.Agency',related_name='Agency_provided_data', blank=True, null=True,on_delete=models.SET_NULL,verbose_name='ชื่อหน่วยงานที่ส่งข้อมูล (ระดับกรม)')
    #GroupActPrb = models.ForeignKey('GroupActPrb',related_name='GroupActPrb', blank=True, null=True,on_delete=models.SET_NULL,verbose_name='กลุ่มข้อมูลตามยุทธศาสตร์ และ พรบ.')
    #GroupActPrb = models.CharField(max_length=4,blank=True, null=True,verbose_name='กลุ่มข้อมูลตามยุทธศาสตร์ และ พรบ.',choices=GroupActPrb_dict)
    GroupActPrb=MultiSelectField(choices=GroupActPrb_dict,blank=True, null=True,verbose_name='กลุ่มข้อมูลตามยุทธศาสตร์ และ พรบ.ทรัพยากรน้ำ พ.ศ.2561')
    keyword = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True,verbose_name='รายละเอียดชุดข้อมูล')
    Time_period = models.TextField(blank=True,verbose_name='ช่วงเวลาของข้อมูล')
    source = models.TextField(blank=True,verbose_name='อธิบายแหล่งข้อมูล')
    type_of_data = models.CharField(
        max_length=3,
        choices=Type_of_data,
        default='UNK',
        verbose_name='รูปแบบชุดข้อมูล',
    )
    date_recived = models.DateTimeField(verbose_name='วันที่ได้รับข้อมูล',blank=True,null=True)
    reference_doc = models.TextField(verbose_name='เอกสารอ้างอิง',blank=True,null=True)
    document01 = models.FileField(upload_to='documents/',verbose_name='เอกสารประกอบ 1',null=True,blank=True)
    document02 = models.FileField(upload_to='documents/',verbose_name='เอกสารประกอบ 2',null=True,blank=True)
    document03 = models.FileField(upload_to='documents/',verbose_name='เอกสารประกอบ 3',null=True,blank=True)
    related_subject = models.TextField(verbose_name='หัวข้อที่เกี่ยวข้อง',blank=True,null=True)
    data_licensing = models.TextField(verbose_name='อธิบายสิทธิของชุดข้อมูล',blank=True,null=True)
    note = models.TextField(verbose_name='โน๊ต',blank=True,null=True)
    status = models.CharField(null=True, blank=True,verbose_name='สถานะการนำไปใช้งานของข้อมูล' ,choices=status_dict,max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


#กลุ่มข้อมูลตามยุทธศาสตร์ และ พรบ.
class GroupActPrb(models.Model):
    class Meta :
        verbose_name='กลุ่มข้อมูล ตามแผนแม่บท และพรบ.ทรัพยากรน้ำพ.ศ.2561'
        verbose_name_plural='กลุ่มข้อมูล ตามแผนแม่บท และพรบ.ทรัพยากรน้ำพ.ศ.2561'
        ordering=('NumOrder',)
    name = models.TextField(verbose_name='ชื่อกลุ่มข้อมูล')
    description = models.TextField(verbose_name='รายละเอียดกลุ่มข้อมูล',null=True)
    NumOrder = models.IntegerField(verbose_name='ลำดับที่')
    def __str__(self):
        return str(self.NumOrder)+') '+self.name