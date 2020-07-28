from rest_framework import serializers
from .models import Rs_Cat
class Rs_CatSerializer(serializers.ModelSerializer):
    def get_field_choices():
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
        return GroupActPrb_dict
    GroupActPrb=serializers.MultipleChoiceField(choices=get_field_choices())
    #document01=serializers.FileField(max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = Rs_Cat
        fields = ('id','name','link','GroupActPrb','note','keyword','status','description','agency','agency_provided_data','Time_period','source','type_of_data','date_recived','reference_doc','document01','document02','document03','related_subject','data_licensing')
        