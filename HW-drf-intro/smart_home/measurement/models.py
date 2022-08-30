from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.TimeField(auto_now_add=True)


class Sensor(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    # measurements = models.ManyToManyField(Measurement, related_name='measurements')
    measurements = models.ManyToManyField(Measurement)

# class SensorMeasurement(models.Model):
#     measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE) #, related_name='positions'
#     sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE) #, related_name='positions'
    # is_main = models.BooleanField(default=False, verbose_name='Основной')