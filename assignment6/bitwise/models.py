from django.db import models

# Create your models here.

class CalculationResult(models.Model):
    input_numbers = models.JSONField()
    result_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'results'
