from django.db import models


class Quarter(models.Model):

    state_code = models.CharField(max_length=2, primary_key=True)
    state = models.CharField(max_length=14)
    year_issued = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    owned = models.BooleanField(default=False)

    def __str__(self):
        return "{}, {}".format(self.state, self.year_issued)
