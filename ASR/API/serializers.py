
from rest_framework import serializers
from .models import ASRText, TTSSound


class ASROutputSeralizer(serializers.ModelSerializer):
    class Meta:
        model = ASRText
        fields = ('uuid', 'name', 'Output','inference_time', 'audio_join_Transformed', 'created_at')


class TTSOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TTSSound
        fields = ('uuid', 'name','text_content', 'audio_join', 'inference_time', 'created_at')