from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class District(models.Model):
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=30)
    duration = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title


class Student(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    mark = models.IntegerField(default=0)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}'
