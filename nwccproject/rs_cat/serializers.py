from rest_framework import serializers
from .models import Rs_Cat
class Rs_CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rs_Cat
        fields = ('id','name','link','GroupActPrb','note','keyword','status','description','agency','agency_provided_data','Time_period','source','type_of_data','date_recived','reference_doc','document01','document02','document03','related_subject','data_licensing')
        