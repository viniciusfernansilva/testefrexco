from django.db import models

# Create your models here.
class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12)

    class Meta:
        db_table = 'region'

    
class Fruit(models.Model):                      
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    regionid = models.ForeignKey(Region, db_column='regionid', on_delete=models.CASCADE)

    class Meta:
        db_table = 'fruit'

