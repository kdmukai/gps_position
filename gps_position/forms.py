from django import forms

from gps_position.models import GPSPosition, GPSArea

"""--------------------------------------------------------------------
    Basic ModelForm for GPSPosition.
--------------------------------------------------------------------"""
class GPSPositionForm(forms.ModelForm):
    class Meta:
        model = GPSPosition


"""--------------------------------------------------------------------
    Basic ModelForm for GPSArea.
--------------------------------------------------------------------"""
class GPSAreaForm(GPSPositionForm):
    class Meta:
        model = GPSArea
        exclude = (
            'max_lat',
            'min_lat',
            'max_lng',
            'min_lng',
        )
