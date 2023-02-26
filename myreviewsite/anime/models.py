from django.db import models

# Create your models here.
#アニメの内容を入れる

CATEGORY = (('fantagy','ファンタジー・SF'),
            ('robot','ロボット・メカ'),
            ('action','アクション・バトル'),
            ('comedy','コメディ・ギャグ'),
            ('love_comedy','恋愛・ラブコメ'),
            ('life','日常・ほのぼの'),
            ('horror','ホラー・サスペンス・推理'),
            ('sports','スポーツ・競技'),
            ('war','戦争・ミリタリー'),
            ('other','その他'),
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
    
    