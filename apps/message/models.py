from django.db import models


# Create your models here.
class UserMessage(models.Model):
    # verbose_name 可以先看成字段的注释

    object_id = models.CharField(max_length=50, default="", primary_key=True, verbose_name=u'主键')
    name = models.CharField(max_length=20, verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=500, verbose_name=u"留言信息")

    # models.IPAddressField
    # models.ForeignKey
    # models.DateTimeField
    # models.FileField
    # models.ImageField
    class Meta:  # 这是什么玩意
        verbose_name = u"用户留言信息"
        verbose_name_plural = verbose_name  # 如果不写这个 会出现用户留言信息s 这种现象
        # db_table = "user_message"
        # ordering = "-object_id"
