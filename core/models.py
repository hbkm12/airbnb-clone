from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # model을 data base에 매번 등록하지 않기위한 class 에 붙여줘야하는 코드
    class Meta:
        abstract = True
