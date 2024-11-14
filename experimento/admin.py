from django.contrib import admin
from .models import Trial,Block, ExperimentSession
# Registra el modelo para que sea visible en la administración
admin.site.register(Trial)
admin.site.register(Block)
admin.site.register(ExperimentSession)