
import uuid
from django.db import models
from .utils import get_path_media, get_path_media_audio_transformation

# Create your models here.
class ASRText(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,null=True, blank=True)
    text_content = models.TextField(null=True, blank=True)
    inference_time = models.CharField(max_length=255,null=True, blank=True)
    # verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "ASRText"
        verbose_name_plural = "ASRTexts"
        # ordering = ["name"]

    def __str__(self):
        return "%s" % self.name

class ASRSound(models.Model):
    audio_file = models.FileField(upload_to='Audio/', null=True, blank=True)


class Sound(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,null=True, blank=True)
    text_content = models.TextField(null=True, blank=True)
    audio_join = models.FileField(upload_to=get_path_media, null=True, blank=True)
    audio_join_Transformed = models.FileField(upload_to=get_path_media_audio_transformation, null=True, blank=True)
    converted = models.BooleanField(default=False)
    #inference_time =  models.TimeField(default=datetime.time(00, 00))
    inference_time = models.CharField(max_length=255,null=True, blank=True)
    inference_time_model_parametre_execution = models.CharField(max_length=255,null=True, blank=True)
    inference_time_audio_saving = models.CharField(max_length=255,null=True, blank=True)
    is_tts = models.BooleanField(default=False)
    is_male = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)