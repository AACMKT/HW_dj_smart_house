from django.urls import path

from measurement.views import MeasurementsCreate, ViewEditSensor, SensorsListCreate

urlpatterns = [
    path('sensors', SensorsListCreate.as_view(), name='AddListSensors'),
    path('measurements', MeasurementsCreate.as_view(), name='AddMeasurement'),
    path('sensors/<pk>', ViewEditSensor.as_view(), name='EditListSensor'),
]
