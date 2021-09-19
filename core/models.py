from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # model�� data base�� �Ź� ������� �ʱ����� class �� �ٿ�����ϴ� �ڵ�
    class Meta:
        abstract = True
