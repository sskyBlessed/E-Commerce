from django.db import models
from django.apps import apps
from users.models import user

class CustomBaseProductModel(models.Model):
     uuid = models.IntegerField(unique=True)
     name = models.CharField(max_length=100)
     price = models.IntegerField()
     description = models.TextField()
     in_stock = models.IntegerField()
     storage = models.IntegerField()
     
     class Meta:
     
         abstract = True
         
class Reviews(models.Model):
    author = models.ForeignKey(user, related_name='review', on_delete=models.CASCADE)
    product = models.ForeignKey(CustomBaseProductModel, related_name='reviews', on_delete=models.CASCADE)
    stars = models.FloatField(default=5.0)
    text = models.CharField(max_length=512)
    


def create_custom_model(model_name, fields):
    class Meta:
        app_label = 'products'
        
    attrs = {'__module__': 'products.models', 'Meta': Meta}
    attrs.update(fields)
    
    return type(model_name, (CustomBaseProductModel,), attrs)
