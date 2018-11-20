from django.db import models


class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

    # 使用管理器来进行创建新对象
    def create(self, title, pub_date):
        b = BookInfo()
        b.btitle = title
        b.bpub_date = pub_date
        b.bread = 0
        b.bcomment = 0
        b.isDelete = False
        return b


# 注意模型类中不要使用__init__方法，因为在Django中Model类的__init__方法做了很多操作
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)

    class Meta(object):
        db_table = 'bookinfo'  # 指定表名
        # ordering = ['id']  # 指定默认排序字段

    books1 = models.Manager()  # 修改默认管理器，取代默认的objects
    books2 = BookInfoManager()  # 自定义管理器对象

    # 使用类方法进行创建新对象，推荐使用管理器方法进行创建
    @classmethod
    def create(cls, title, pub_date):
        b = BookInfo()
        b.btitle = title
        b.bpub_date = pub_date
        b.bread = 0
        b.bcomment = 0
        b.isDelete = False
        return b


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def showname(self):
        return self.hname
