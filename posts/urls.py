from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ホームページ
    path('create/', views.create_facility, name='create_facility'),  # 施設投稿フォームページ
    path('facility/<int:facility_id>/', views.facility_detail, name='facility_detail'),  # 施設の詳細ページ
    path('facility/<int:facility_id>/review/', views.create_review, name='create_review'),  # レビューフォームページ
    path('select-category/', views.select_category, name='select_category'),  # カテゴリ選択ページのURL追加
]
