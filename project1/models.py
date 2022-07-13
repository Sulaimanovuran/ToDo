from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BuyProduct(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyproduct')
    title = models.CharField(max_length=50)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['create_date']

    def __str__(self):
        return f'{self.title} <---> {self.owner}'
