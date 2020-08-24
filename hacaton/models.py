from django.db import models


# Create your models here.
class AR_Work(models.Model):
    field_user = models.IntegerField()
    field_count = models.IntegerField()
    field_views = models.IntegerField()

    def __str__(self):
        return 'Ar workers' + str(self.field_count)