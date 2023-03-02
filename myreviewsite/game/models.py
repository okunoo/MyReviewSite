from django.db import models

# Create your models here.
#ゲームの内容を入れる
CATEGORY = (('シューティング','シューティング'),
            ('アクション','アクション'),
            ('ロールプレイング','ロールプレイング'),
            ('アドベンチャー','アドベンチャー'),
            ('レース','レース'),
            ('シミュレーション','シミュレーション'),
            ('ホラー','ホラー・サスペンス・推理'),
            ('サンドボックス','サンドボックス'),
            ('音楽','音楽'),
            ('テーブル','テーブル'),
            ('その他','その他'),
        )

class Game(models.Model):
    #ゲームの題名
    name = models.CharField(max_length=100)
    #ゲームの概要
    overview = models.TextField()
    #ゲームの画像
    thumbnail = models.ImageField(null = True,blank = True)
    #作者のコメント
    comment = models.TextField(default="無し")
    #ゲームのメインカテゴリー
    main_category = models.CharField(
        max_length=100,
        choices=CATEGORY,
    )
    #ゲームのスコア
    score = models.IntegerField()
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Game_Review(models.Model):
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    comment = models.TextField()
    score = models.IntegerField()
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    
    