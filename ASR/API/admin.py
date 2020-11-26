
from django.contrib import admin
from .models import ASRText, TTSSound

# Register your models here.
admin.site.register(ASRText)
admin.site.register(TTSSound)