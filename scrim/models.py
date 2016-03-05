from django.db import models


class Scrim(models.Model):
    team_name = models.CharField(max_length=64)
    team_captain = models.CharField(max_length=64)
    region = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.team_name
