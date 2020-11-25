
from rest_framework import serializers
from .models import ASRText, Sound


class SoundSerializerIn(serializers.ModelSerializer):
    #extra_fields = ExtraFieldContentSerializerOut(many=True)
    class Meta:
        model = ASRText
        fields = ('uuid', 'name','text_content','inference_time' ,'updated_at', 'created_at')


class SoundSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ('uuid', 'name','text_content','audio_join','audio_join_Transformed','is_male','inference_time' ,'converted','created_at', 'updated_at' )
