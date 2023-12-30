from django.contrib import admin
from .models import UploadedSelfie
from .models import Images

# Register your models here.


admin.site.register(UploadedSelfie)

admin.site.register(Images)
