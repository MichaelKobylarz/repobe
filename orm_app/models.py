from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Country(models.Model):
    name = models.CharField(max_length=255)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)


class Capital(models.Model):
    name = models.CharField(max_length=255)


class Language(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
