from enum import unique
from django.contrib.auth.models import User
from projectapp import models as projectappModels
from django.db import models


# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscription"
    )
    project = models.ForeignKey(
        projectappModels.Project, on_delete=models.CASCADE, related_name="subscription"
    )

    class Meta:
        unique_together = ("user", "project")  # 👈 user와 project가 이루는 쌍은 오직 1개만 이뤄지도록!
