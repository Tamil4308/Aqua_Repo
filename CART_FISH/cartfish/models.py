from django.db import models
from django.urls import reverse

# Create your models here.

class Aqua(models.Model):
    image = models.ImageField(upload_to='media')
    fishname = models.CharField(max_length=40)
    orgin = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()

    class META:
        t_table = 'Aqua'

    def get_absolute_url(self):
        return reverse('list')
    
class Post(models.Model):
	NAME = models.CharField( max_length = 20, blank = False,null = False)

	MOBILE_NO = models.BigIntegerField(null=False)

	# This is used to write a post
	ENQUIRE = models.TextField(blank = False, null = False)


	
	# Values for gender are restricted by giving choices
	#gender = models.CharField(max_length = 6, choices = GENDER_CHOICES,default = Male)
	
	time = models.DateTimeField(auto_now_add=True)