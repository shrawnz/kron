from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from collections import OrderedDict
from kronFrame.forms import CourseForm

from .models import *
from pprint import pprint

class IndexView(generic.ListView):
	template_name = 'kronFrame/index.html'
	context_object_name = 'courseList'

	def get_queryset(self):
		courseList = {}
		for x in Offered.objects.all():
			if x.course not in courseList: courseList[x.course] = [x]
			else: courseList[x.course].append(x)
		print courseList
		return courseList

class HomeView(generic.ListView):
	template_name = 'kronFrame/home.html'
	context_object_name = 'dataSet'

	def get_queryset(self):
		dataSet = {}
		dataSet['table'] = OrderedDict([('Mon',OrderedDict()),('Tue',OrderedDict()),('Wed',OrderedDict()),('Thu',OrderedDict()),('Fri',OrderedDict()),('Sat',OrderedDict())])
		dataSet['ourDays'] = dict([('Mon',"Monday"),('Tue',"Tuesday"),('Wed',"Wednesday"),('Thu',"Thursday"),('Fri',"Friday"),('Sat',"Saturday")])
		dataSet['choice'] = set()
		dataSet['times'] = [" "]
		for x in range(1,len(Offered.TIME_CHOICES)):
			dataSet['times'].append(Offered.TIME_CHOICES[x][1])
		for day in dataSet['table'].keys():
			for seg in range(20):
				dataSet['table'][day][seg+2] = []
		for x in Offered.objects.all():
			for allSeg in range(int(x.start_time),int(x.end_time)):
				if(x.course.acronym not in dataSet['table'][x.class_day][allSeg]):
					x.woah = ""
					for y in x.callSign.all():
						dataSet['choice'].add(y.sign)
						x.woah += y.sign+" "
					dataSet['table'][x.class_day][allSeg].append(x)
		dataSet['choice'] = sorted(list(dataSet['choice']))
		pprint(dataSet['choice'])
		text = "YOOOOOOO"
		return text

class PopulateView(generic.DetailView):
	template_name = 'kronFrame/populate.html'

	def get(self,request):
		print ("HERE")
		text = "HeCk"
		courseForm = CourseForm()
		course_list = Course.objects.all()
		return render(self.request, self.template_name, {'form':courseForm,'text':text,'list':course_list})

	def post(self, request, *args, **kwargs):
		print (request.POST)
		# courseForm = CourseForm(request.POST)
		# if courseForm.is_valid():
		# 	courseForm.save()
		# 	course = Course.objects.filter(course_id=request.POST['course_id']);
		# 	print course
		# 	inst = Instructor(name=request.POST['instructor'],course=course)
		new_form = CourseForm()
		course_list = Course.objects.all()
		return render(request, self.template_name, {'form':new_form,'list':course_list})