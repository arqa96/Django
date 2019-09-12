from django.db import models
from django.utils import timezone


class CarBrand(models.Model):

	brand = models.CharField(max_length=20)
	model = models.CharField(max_length=20)
	body = models.CharField(max_length=20)
	transmission = models.CharField(max_length=20)
	engine = models.CharField(max_length=20)
	drive = models.CharField(max_length=20)
	year = models.IntegerField()
	mileage = models.CharField(max_length=20)
	price = models.IntegerField()
	comments = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	image = models.ImageField(default='default.png', upload_to='auto_pics')

	def __str__(self):
		return f'{self.brand} {self.model}'

	class Meta:
		verbose_name = 'car'
		verbose_name_plural = 'cars'








