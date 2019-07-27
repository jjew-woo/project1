from django.db import models

# Create your models here.

class KoreanFood(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    area = models.CharField(max_length=10, default = "송파구")
    star = models.IntegerField()

    def __str__(self):
        return self.title

class ChineseFood(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    area = models.CharField(max_length=10,  default = "송파구")
    star = models.IntegerField()

    def __str__(self):
        return self.title

class JapaneseFood(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    area = models.CharField(max_length=10,  default = "송파구")
    star = models.IntegerField()


    def __str__(self):
        return self.title

class WesternFood(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    area = models.CharField(max_length=10 ,  default = "송파구")
    star = models.IntegerField()
    

    def __str__(self):
        return self.title

class FastFood(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    area = models.CharField(max_length=10,  default = "송파구")
    star = models.IntegerField()

    def __str__(self):
        return self.title

class Dessert(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    area = models.CharField(max_length=10,  default = "송파구")
    star = models.IntegerField()

    def __str__(self):
        return self.title

class Drink(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    area = models.CharField(max_length=10,  default = "송파구")
    star = models.IntegerField()

    def __str__(self):
        return self.title