from django.db import models
from alfuhigi.models import ContentTypeAbstract, CreateAbstract
# Create your models here.


class Marker(ContentTypeAbstract, CreateAbstract):
    name = models.CharField(max_length=100, null=True, blank=True)
    descr = models.CharField(max_length=100, null=True, blank=True)
    lat = models.CharField(max_length=100,)
    lng = models.CharField(max_length=100,)

    def as_dict(self):
        return {
            'date': str(self.create_at),
            "name": self.name,
            'descr': self.descr,
            'lat': self.lat,
            'lng': self.lng,
            }
