from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=100)
	course_id = models.CharField(max_length=25)
	acronym = models.CharField(max_length=10, primary_key=True)
	CREDS = (
		(2,'2 Credits'),
		(4, '4 Credits'),
	)
	credits = models.IntegerField(choices=CREDS, default=4)
	
	CATEGORY_CSE=1
	CATEGORY_ECE=2
	CATEGORY_MTH=3
	CATEGORY_HSS=4
	CATEGORY_BIO=5
	CATEGORY_ECO=6
	CATEGORY_OTH=7
	
	CATEGORIES = (
		(CATEGORY_CSE,'CSE'),
		(CATEGORY_ECE,'ECE'),
		(CATEGORY_MTH,'MTH'),
		(CATEGORY_HSS,'HSS'),
		(CATEGORY_BIO,'BIO'),
		(CATEGORY_ECO,'ECO'),
		(CATEGORY_OTH,'OTH')
	)
	
	category = models.IntegerField(choices=CATEGORIES, default=CATEGORY_CSE) 
	
	TYPE = (
		(1,'Mandatory'),
		(2, 'Elective')
	)
	choice_type = models.IntegerField(choices=TYPE, default=2)
	semester = models.IntegerField(null=True)

	def __str__(self):
		return self.acronym

class Prerequisites(models.Model):
	name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='prereqs')
	prerequisite = models.ManyToManyField(Course)

	def __str__(self):
		return self.name

class Instructor(models.Model):
	name = models.CharField(max_length=50)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='instructor')

	def __str__(self):
		return self.name

class Offered(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	
	TYPE = (
		(1,'Lecture'),
		(2,'Tutorial'),
		(3,'Lab')
	)
	class_type = models.IntegerField(choices=TYPE,default=1)

	areaName = models.CharField(max_length=50)
	DAYS = (
		('Mon','Monday'),
		('Tue','Tuesday'),
		('Wed','Wednesday'),
		('Thu','Thursday'),
		('Fri','Friday'),
		('Sat','Saturday'),
	)
	TIME_CHOICES = (
		('1', "08:00"),
		('2', "08:30"),
		('3', "09:00"),
		('4', "09:30"),
		('5', "10:00"),
		('6', "10:30"),
		('7', "11:00"),
		('8', "11:30"),
		('9', "12:00"),
		('10', "12:30"),
		('11', "13:00"),
		('12', "13:30"),
		('13', "14:00"),
		('14', "14:30"),
		('15', "15:00"),
		('16', "15:30"),
		('17', "16:00"),
		('18', "16:30"),
		('19', "17:00"),
		('20', "17:30"),
		('21', "18:00"),
		('22', "18:30"),
	)
	class_day = models.CharField(max_length=3, choices=DAYS, default='Mon')
	start_time = models.CharField(max_length=2,choices=TIME_CHOICES, default=1)
	end_time = models.CharField(max_length=2,choices=TIME_CHOICES, default=1)
	def __str__(self):
		return str(self.course)+": "+str(self.class_day)+","+str(self.get_start_time_display())+" to "+str(self.get_end_time_display())
