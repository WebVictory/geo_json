from django.db.models import Q
from django.http import JsonResponse
from rest_framework import mixins, status, filters, views
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from geo_api.models import Polygon, LineString, Point
from geo_api.serializers import PolygonSerializer, LineStringSerializer


class PolygonViewSet(ModelViewSet):
    """
    API endpoint working with Polygon
    """
    serializer_class = PolygonSerializer
    queryset = qs = Polygon.objects.prefetch_related('points')
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name']


class LineStringViewSet(ModelViewSet):
    """
    API endpoint working with LineString
    """
    serializer_class = LineStringSerializer
    queryset = LineString.objects.all()
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name']


class PointViewSet(ModelViewSet):
    """
    API endpoint working with Point
    """
    serializer_class = LineStringSerializer
    queryset = Point.objects.all()
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name']


from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer


# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        name = request.POST.get('name')
        import gpxpy
        import gpxpy.gpx

        # Parsing an existing file:
        # -------------------------

        # gpx_file = open('test_files/cerknicko-jezero.gpx', 'r')

        gpx = gpxpy.parse(file_uploaded)

        import json
        from django.contrib.gis.geos import GEOSGeometry

        # data_coordinates = [[36.66678428649903, -1.5474249907643578], [36.670904159545906, -1.542620219636788],
        #                     [36.66635513305665, -1.5353272427374922], [36.662406921386726, -1.5403894293513378]]
        #
        # for coordinate in data_coordinates:
        #     point = {
        #         "type": "Point",
        #         "coordinates": coordinate
        #     }
        #
        #     Point.objects.create(name="your location name", geometry=GEOSGeometry(json.dumps(point)))

        for track in gpx.tracks:
            for segment in track.segments:
                for i, point in enumerate(segment.points):
                    point = {
                        "type": "Point",
                        "coordinates": [point.latitude, point.longitude]
                    }
                    Point.objects.create(name=name + str(i), geometry=GEOSGeometry(json.dumps(point)))
                    # print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

        for waypoint in gpx.waypoints:
            print('waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude))

        for route in gpx.routes:
            print('Route:')
            for point in route.points:
                print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

        # There are many more utility methods and functions:
        # You can manipulate/add/remove tracks, segments, points, waypoints and routes and
        # get the GPX XML file from the resulting object:

        print('GPX:', gpx.to_xml())

        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)


# views.py
class FileUploadView(views.APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)
