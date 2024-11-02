from django import forms
from .models import Facility, Review

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = [
            'facility_name', 'address', 'phone_number', 'website_url', 'category',
            'diaper_changing', 'nursing_room', 'kids_space', 'wheelchair_access',
            'baby_car_rental', 'parking', 'description'
        ]

class RecipeForm(FacilityForm):
    ingredients = forms.CharField(widget=forms.Textarea, required=False, label='レシピの材料')

    class Meta(FacilityForm.Meta):
        fields = FacilityForm.Meta.fields + ['ingredients']

class ParkForm(FacilityForm):
    playground = forms.BooleanField(required=False, label='遊具の有無')
    park_features = forms.CharField(widget=forms.Textarea, required=False, label='公園の特徴')

    class Meta(FacilityForm.Meta):
        fields = FacilityForm.Meta.fields + ['playground', 'park_features']

# ReviewForm を追加
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
