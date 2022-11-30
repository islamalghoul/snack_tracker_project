from django.db import models
from django.contrib.auth import get_user_model
class Snack (models.Model):
    name=models.CharField(max_length=64,default='snacks')
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    discreption=models.TextField(default="apple")

    def __str__(self) -> str:
        return self.name