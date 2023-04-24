from django.db import models

# Create your models here.
class User(models.Model):
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField()
    diet_recommendations = models.TextField()
    exercise_recommendations = models.TextField()
    test_recommendations = models.TextField()

    def __str__(self):
        return f"User: height={self.height}, weight={self.weight}, bmi={self.bmi}, diet_recommendations={self.diet_recommendations}, exercise_recommendations={self.exercise_recommendations}, test_recommendations={self.test_recommendations}"
