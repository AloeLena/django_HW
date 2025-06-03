from django.db import models

class Sensor(models.Model):

    name = models.CharField(max_length=100, help_text="Название датчика")
    description = models.TextField(
        null=True, blank=True, help_text="Описание датчика"
    )

    def __str__(self):
        return f"{self.name}: {self.description or 'No description'}"


class Measurement(models.Model):
    # Поле sensor - внешний ключ к модели Sensor
    # related_name='measurements' позволяет обратиться к измерениям датчика через sensor.measurements.all()
    # on_delete=models.CASCADE означает, что при удалении датчика все его измерения также будут удалены
    sensor = models.ForeignKey(
        Sensor,
        related_name="measurements",
        on_delete=models.CASCADE,
        help_text="Связанный датчик",
    )

    # Поле temperature - числовое поле для хранения температуры
    temperature = models.FloatField(help_text="Измеренная температура")

    # Поле created_at - дата и время создания записи
    # auto_now_add=True автоматически устанавливает текущую дату и время при создании объекта
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Дата и время измерения"
    )

    # Поле image - поле для хранения изображений
    # null=True и blank=True позволяют оставлять это поле пустым
    image = models.ImageField(
        upload_to="sensor_measurements/",
        null=True,
        blank=True,
        help_text="Изображение измерения",
    )

    def __str__(self):
        return f"Измерение датчика {self.sensor.name}: {self.created_at}"