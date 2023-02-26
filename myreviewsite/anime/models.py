from django.db import models

# Create your models here.
#アニメの内容を入れる

CATEGORY = (('ファンタジー','ファンタジー・SF'),
            ('ロボット','ロボット・メカ'),
            ('アクション','アクション・バトル'),
            ('コメディ','コメディ・ギャグ'),
            ('恋愛・ラブコメディ','恋愛・ラブコメ'),
            ('日常','日常・ほのぼの'),
            ('ホラー','ホラー・サスペンス・推理'),
            ('スポーツ','スポーツ・競技'),
            ('戦争・ミリタリー','戦争・ミリタリー'),
            ('学園','学園'),
            ('その他','その他'),
        )

class Anime(models.Model):
    #アニメの題名
    name = models.CharField(max_length=100)
    #アニメの概要
    overview = models.TextField()
    #アニメの画像
    thumbnail = models.ImageField(null = True,blank = True)
    #作者のコメント
    comment = models.TextField(default="無し")
    #アニメのメインカテゴリー
    main_category = models.CharField(
        max_length=100,
        choices=CATEGORY,
    )
    #サブのカテゴリー
    sub_category = models.CharField(
        max_length=100,
        choices=CATEGORY,
        null = True,
        blank=True,
    )
    #アニメのスコア
    score = models.IntegerField()
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Review(models.Model):
    anime = models.ForeignKey(Anime,on_delete=models.CASCADE)
    comment = models.TextField()
    score = models.IntegerField()
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    
    