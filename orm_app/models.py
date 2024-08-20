from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


# 1 to 1
class Country(models.Model):
    name = models.CharField(max_length=255)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)


class Capital(models.Model):
    name = models.CharField(max_length=255)


# 1 to many
class Language(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# many to many
class Actor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    actors = models.ManyToManyField('Actor')

    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=128)

    def str(self):
        return self.name

class Band(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def str(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Band, on_delete=models.CASCADE)
    date_joined = models.DateField()

class Product(models.Model):
    title = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.IntegerField()

    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)

    product_secret_id = models.CharField(max_length=100)