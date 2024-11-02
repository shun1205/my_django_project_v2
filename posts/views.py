from django.shortcuts import render, redirect, get_object_or_404
from .forms import FacilityForm, RecipeForm, ParkForm, ReviewForm  # 各カテゴリに応じたフォームをインポート
from .models import Facility

def home(request):
    # クエリパラメータの取得
    area = request.GET.get('area', '')  # エリアのフィルタリング条件
    category = request.GET.get('category', '')  # カテゴリのフィルタリング条件
    keyword = request.GET.get('keyword', '')  # キーワードのフィルタリング条件

    # 基本クエリセット
    facilities = Facility.objects.all()

    # エリアでのフィルタリング
    if area:
        facilities = facilities.filter(address__icontains=area)

    # カテゴリでのフィルタリング
    if category:
        facilities = facilities.filter(category=category)

    # キーワードでのフィルタリング
    if keyword:
        facilities = facilities.filter(description__icontains=keyword)

    # フィルタリングされた施設のリストを表示
    return render(request, 'posts/home.html', {'facilities': facilities})

def create_facility(request):
    initial_data = {}
    if 'category' in request.GET:
        initial_data['category'] = request.GET['category']

    if request.method == 'POST':
        # カテゴリに応じたフォームを使うようにする
        form_class = get_form_class(request.POST.get('category', ''))
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # 投稿後にホームページにリダイレクトします
    else:
        form_class = get_form_class(initial_data.get('category', ''))
        form = form_class(initial=initial_data)
    return render(request, 'posts/facility_form.html', {'form': form})

def get_form_class(category):
    # カテゴリに応じたフォームクラスを返す関数
    if category == 'recipe':
        return RecipeForm
    elif category == 'park':
        return ParkForm
    else:
        return FacilityForm

def facility_detail(request, facility_id):
    facility = get_object_or_404(Facility, pk=facility_id)
    reviews = facility.reviews.all()  # この施設に関連する全てのレビューを取得
    return render(request, 'posts/facility_detail.html', {'facility': facility, 'reviews': reviews})

def create_review(request, facility_id):
    facility = get_object_or_404(Facility, pk=facility_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.facility = facility
            review.save()
            return redirect('facility_detail', facility_id=facility.pk)  # 投稿後に施設の詳細ページにリダイレクト
    else:
        form = ReviewForm()
    return render(request, 'posts/review_form.html', {'form': form, 'facility': facility})

def select_category(request):
    # カテゴリ選択用のテンプレートを表示するビュー
    return render(request, 'posts/select_category.html')
