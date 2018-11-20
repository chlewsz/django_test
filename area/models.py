from django.db import models


class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parea = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta(object):
        db_table = 'areainfo'

