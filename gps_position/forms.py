from django import forms

from gps_position.models import GPSPosition, GPSArea

class GPSPositionForm(forms.ModelForm):
    class Meta:
        model = GPSPosition


class GPSAreaForm(GPSPositionForm):
    class Meta:
        model = GPSArea
        exclude = (
            'max_lat',
            'min_lat',
            'max_lng',
            'min_lng',
        )
