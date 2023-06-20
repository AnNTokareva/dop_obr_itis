from django.db import models


class AnalysisResult(models.Model):
    age = models.IntegerField(default=0)
    creatinine_phosphokinase = models.IntegerField(default=0)
    ejection_fraction = models.IntegerField(default=0)
    platelets = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    death_event = models.IntegerField(blank=True, default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Результаты анализов'

    def __str__(self):
        return str(self.death_event)
