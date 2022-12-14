from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CustomUser(AbstractUser):
    fav_color = models.CharField(blank=True, max_length=120)

    def __str__(self):
        return str(self.id) + ' ' + self.username

class Criteria(models.Model):
    user_id = models.OneToOneField('CustomUser', on_delete=models.PROTECT)
    beds = models.PositiveIntegerField(default=0, null=False)
    baths = models.PositiveIntegerField(default=0 )
    min_price = models.DecimalField(default=0, max_digits=9, decimal_places=0)
    max_price = models.DecimalField(default=99999999999999, max_digits=15, decimal_places=0, null=True)
    sqft = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.user_id) + ' ' + str(self.beds) + ' ' + str(self.baths) + ' ' + str(self.min_price) + ' ' + str(self.max_price) + ' ' + str(self.sqft)


class LikedHouses(models.Model):
    user_id = models.ForeignKey('CustomUser', on_delete=models.PROTECT)
    house_id = models.IntegerField(null=False)

    def __str__(self):
        return str(self.user_id) + ' House ID || ' + str(self.house_id)

