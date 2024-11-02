from django import forms
from .models import Facility, Review

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = [
            'facility_name',
            'address',
            'phone_number',
            'website_url',
            'category',
            'diaper_changing',
            'nursing_room',
            'kids_space',
            'wheelchair_access',
            'baby_car_rental',
            'parking',
            'description',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
