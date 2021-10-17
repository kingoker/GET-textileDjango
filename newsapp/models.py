from django.db import models



class Service(models.Model):
	icon = models.ImageField(upload_to="services/%Y/%m/%d")
	title = models.CharField(max_length=255)
	description = models.TextField()

class New(models.Model):
	image = models.ImageField(upload_to="news/%Y/%m/%d")
	title = models.CharField(max_length=255)
	text = models.TextField()
	date = models.DateTimeField()
	is_publish = models.BooleanField(default=False)


class Person(models.Model):
	image = models.ImageField(upload_to="persons/%Y/%m/%d")
	name = models.CharField(max_length=255)
	occupation = models.CharField(max_length=255)
	facebook = models.URLField()
	instagram = models.URLField()	
	linkedin = models.URLField()	

class Partner(models.Model):
	image = models.ImageField(upload_to="partners/%Y/%m/%d")
	name = models.CharField(max_length=255)
	description = models.TextField()


class Comment(models.Model):
	name = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	comment = models.TextField()