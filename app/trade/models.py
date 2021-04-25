from django.db import models


class ShrimpyLeader(models.Model):
    """
    https://www.shrimpy.io/api/leaders
    """
    uid = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    picture_hash = models.CharField(max_length=255)
    exchange = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    performance_day = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    performance_week = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    performance_month = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    followers_count = models.PositiveIntegerField(default=0)
    is_paid = models.BooleanField()
    creation_date = models.DateField(auto_now_add=True)
    last_access_date = models.DateTimeField()

    @property
    def picture(self):
        return self.get_picture()

    def get_picture(self, size=64):
        if self.picture_hash:
            return f"https://assets.shrimpy.io/leader_profile_picture/{self.picture_hash}/{size}.png"
        else:
            return "/static/images/c.svg"

    def __str__(self):
        return self.name
