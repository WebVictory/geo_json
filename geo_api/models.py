from django.db import models as old_models
from django.contrib.gis.db import models
# Create your models here.


class Polygon (models.Model):
    name = models.CharField("Имя", max_length=100)
    geometry = models.PolygonField("Полигон")

    def __str__(self):
        return self.name

class LineString (models.Model):
    name = models.CharField("Имя", max_length=100)
    geometry = models.LineStringField("Линия")

    def __str__(self):
        return self.name

class Point (models.Model):
    name = models.CharField("Имя", max_length=100)
    # geometry = models.PointField("Геометрия")
    geometry = models.PointField("Точка",)
    polygon = models.ManyToManyField("Polygon", related_name='points')

    def __str__(self):
        return self.name
