# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from measurement.models import  Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer


# class DemoSensorView(ListAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
#     def post(self, request):
#         sensor = Sensor(name=request.data.get('name'), description=request.data.get('description'))
#         sensor.save()
#         return Response({"status": "ok"})
#     #
#     def get(self, request):
#         queryset = Sensor.objects.all()
#         serializer_class = SensorSerializer(queryset, many=True)
#         return Response(serializer_class.data)
#         # return Response(request.GET)


class SensorView(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementView(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer



