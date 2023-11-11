from django.db import models

# Create your models here.

class Grading_Results(models.Model):
    Question = models.CharField(max_length=255)
    Choice_Field = models.CharField(max_length=255)
    Votes = models.IntegerField()


    def __str__(self):
        return f"{self.Question} {self.Choice_Field}"