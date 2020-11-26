import uuid
from django.db import models
from .utils import get_tts_media, get_asr_media

# Create your models here.
class ASRText(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,null=True, blank=True)
    Output = models.TextField(null=True, blank=True)
    inference_time = models.CharField(max_length=255,null=True, blank=True)
    audio_join_Transformed = models.FileField(upload_to=get_asr_media, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "ASRText"
        verbose_name_plural = "ASRTexts"
        # ordering = ["name"]

    def __str__(self):
        return "%s" % self.name

class ASRInputSound(models.Model):
    audio_file = models.FileField(upload_to='ASR_Input/', null=True, blank=True)


class TTSSound(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,null=True, blank=True)
    text_content = models.TextField(null=True, blank=True)
    audio_join = models.FileField(upload_to=get_tts_media, null=True, blank=True)
    inference_time = models.CharField(max_length=255,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

