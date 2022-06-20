from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=30,primary_key=True)
    slug=models.SlugField(null=True, blank=True)
    alpha2=models.CharField(max_length=2)
    alpha3=models.CharField(max_length=3)
    countrycode=models.IntegerField()
    region=models.CharField(max_length=30,blank=True)
    subregion=models.CharField(max_length=30,blank=True)
    interregion=models.CharField(max_length=30,blank=True)
    regioncode=models.IntegerField(blank=True,null=True)
    subregioncode=models.IntegerField(blank=True, null=True)
    interregioncode=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        self.slug=slugify(self.name)
        super(Country, self).save(*args, **kwargs)
    