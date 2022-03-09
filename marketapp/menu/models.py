from django.db import models


class MarketName(models.Model): # darital
	name  = models.CharField(max_length=200)
	typeOfMagazine = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name

class MenuObject(models.Model): # cola
	title = models.CharField(max_length=200) #cola
	img = models.ImageField(upload_to='media') #cola.img
	price = models.IntegerField() #15000
	boss = models.ForeignKey(MarketName, on_delete=models.CASCADE)


	def __str__(self):
		return self.title
