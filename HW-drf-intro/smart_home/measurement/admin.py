from django.contrib import admin

# Register your models here.
from measurement.models import Measurement, Sensor#, SensorMeasurement


# class RelationshipInline(admin.TabularInline):

    # model = SensorMeasurement
    # list_display = ['id', 'name']
    # formset = RelationshipInlineFormset


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass
    list_display = ['id', 'temperature', 'created_at']

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass
    list_display = ['id', 'name', 'description']
    # inlines = [RelationshipInline]