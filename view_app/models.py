from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} z {self.city} ({self.age})"

    # # można też w taki sposób (zamiast success_url w CreateView)
    # def get_absolute_url(self):
    #     return 'view_app:create_person_view2'
