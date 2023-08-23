from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return str(self.pk)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')

    class Meta:
        verbose_name = 'Измерения'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return f' sensor: {self.sensor} | temperature: {self.temperature}'
