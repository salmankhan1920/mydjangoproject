from django import forms
from .models import UploadedSelfie, Images

from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField



class SelfieForm(forms.ModelForm):
    class Meta:
        model = UploadedSelfie
        fields = ['selfie']




class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image']




class UploadForm(forms.Form):
    # For images (requires Pillow for validation):
    attachments = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)