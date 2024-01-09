from rest_framework import serializers
from .models import Program

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['name','Location','date','Dress_code','Venue','Description','start_time','cover_photo']