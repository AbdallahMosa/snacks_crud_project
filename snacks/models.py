from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Snack(models.Model):
    title = models.CharField(max_length=255)
    purchaser= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description =models.TextField(default="description")

    def __str__(self) :
        return self.title

    class Meta:
        verbose_name_plural ='my snacks'
        ordering=['pk']
    def get_absolute_url(self):
        return reverse("snack_detail",args=[self.id])