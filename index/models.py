from django.db import models

# Create your models here.
class Stock(models.Model):
    type=models.CharField(max_length=20)
    code=models.CharField(max_length=50)
class StockData(models.Model):
    name=models.CharField(max_length=20)
    start=models.FloatField()
    yesterday=models.FloatField()
    now=models.FloatField()
    high=models.FloatField()
    low=models.FloatField()
    now_plus=models.FloatField()
    now_minus=models.FloatField()
    counts=models.IntegerField()
    money=models.IntegerField()
    datetime=models.DateTimeField()
    stock=models.ForeignKey(Stock)
    
    