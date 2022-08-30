from django.urls import path
from measurement.views import SensorView, MeasurementView
from django.contrib import admin
from django.urls import path



# from demo.views import DemoView, SensorView
snippet_list_sensors = SensorView.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail_sensors = SensorView.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    # 'delete': 'destroy'
})

snippet_list_measurement = MeasurementView.as_view({
       'get': 'list',
    'post': 'create'
})

snippet_detail_measurement = MeasurementView.as_view({
       'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    # 'delete': 'destroy'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/<pk>/', snippet_detail_sensors),
    path('sensors/', snippet_list_sensors),
    path('measurements/<pk>/', snippet_detail_measurement),
    path('measurements/', snippet_list_measurement),

]

