# family_info_sharing/urls.py (プロジェクトレベルのurls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),  # postsアプリのURLパターンをインクルード
]
