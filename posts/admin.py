from django.contrib import admin
from .models import Facility, Review

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('facility_name', 'address', 'category', 'diaper_changing', 'nursing_room')
    search_fields = ('facility_name', 'address')
    list_filter = ('category', 'diaper_changing', 'nursing_room')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'facility', 'rating', 'comment')
    search_fields = ('user__username', 'facility__facility_name')
    list_filter = ('rating',)
