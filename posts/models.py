from django.db import models

CATEGORY_CHOICES = [
    ('restaurant', '飲食店'),
    ('recipe', 'レシピ'),
    ('park', '公園'),
    ('activity', 'アクティビティ'),
    ('support', '地域の支援'),
    ('education', '教育'),
    ('school', '学校'),
    ('experience', '経験談'),
]

class Facility(models.Model):

    
    facility_name = models.CharField(max_length=100, verbose_name='施設名')
    address = models.CharField(max_length=255, verbose_name='住所')
    phone_number = models.CharField(max_length=20, blank=True, verbose_name='電話番号')
    website_url = models.URLField(blank=True, verbose_name='ウェブサイトURL')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name='カテゴリ', null=True)  # <--- ここを修正します
    diaper_changing = models.BooleanField(default=False, verbose_name='おむつ替え台の有無')
    nursing_room = models.BooleanField(default=False, verbose_name='授乳室の有無')
    kids_space = models.BooleanField(default=False, verbose_name='キッズスペースの有無')
    wheelchair_access = models.BooleanField(default=False, verbose_name='バリアフリー対応')
    baby_car_rental = models.BooleanField(default=False, verbose_name='ベビーカーの貸し出し')
    parking = models.BooleanField(default=False, verbose_name='駐車場の有無')
    description = models.TextField(blank=True, verbose_name='説明')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.facility_name


class Review(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='コメント')
    rating = models.IntegerField(verbose_name='評価（1〜5）', choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f"{self.user.username} - {self.facility.facility_name}"
