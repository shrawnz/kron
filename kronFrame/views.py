from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from collections import OrderedDict
from kronFrame.forms import CourseForm, OfferedForm
from .models import *
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import datetime
from collections import defaultdict

class IndexView(generic.ListView):
	template_name = 'kronFrame/index.html'
	context_object_name = 'courseList'

	def get_queryset(self):
		courseList = {}
		for x in Offered.objects.all():
			if x.course not in courseList: courseList[x.course] = [x]
			else: courseList[x.course].append(x)
		print (courseList)
		return courseList

class HomeView(generic.DetailView):
	template_name = 'kronFrame/home.html'
	context_object_name = 'dataSet'

	def get(self, request):
		offs = Offered.objects.all()
		courses = Course.objects.all()

		offered_dict = defaultdict(list)
		# course_dict = defaultdict(list)
		course_list = []
		
		for i in offs:
			course = i.course
			start = i.start_time
			end = i.end_time
			typ = i.class_type
			day = i.class_day
			
			offered_dict[course.cid].append([Offered.TIME_CHOICES[start-1][1], Offered.TIME_CHOICES[end-1][1], Offered.TYPE[typ-1][1], Offered.DAY_CHOICES[day-1][1]])


		for i in courses:
			cid = i.cid
			category = 'OTH'
			for k,v in Course.CATEGORIES:
				if k == i.category:
					category = v
			name = i.name
			inst = Instructor.objects.filter(course=i).first()	
			course_list.append([cid, name, inst.name, category])

		return render(request, self.template_name, {'courses': course_list, 'offered':dict(offered_dict)})

class PopulateView(generic.DetailView):
	template_name = 'kronFrame/index.html'

	def get(self,request):
		print ("HERE")
		text = "HeCk"
		choices = Offered.TIME_CHOICES
		print (choices)
		days = Offered.DAY_CHOICES
		courseForm = CourseForm()
		course_list = Course.objects.all()
		return render(self.request, self.template_name, {'days':days,'time':choices,'form':courseForm,'text':text,'list':course_list})

	def post(self, request, *args, **kwargs):
		print (request.POST)
		courseForm = CourseForm(request.POST)
		if courseForm.is_valid():
			courseForm.save()
			course = Course.objects.filter(course_id=request.POST['course_id']).first();
			inst = Instructor(name=request.POST['instructor'],course=course)
			inst.save()
		new_form = CourseForm()
		course_list = Course.objects.all()
		return render(request, self.template_name, {'form':new_form,'list':course_list})

class OfferedView(generic.DetailView):
	template_name = 'kronFrame/offered.html'

	def get(self,request):
		print ("HERE")
		text = "HeCk"
		form = OfferedForm()
		course_list = Course.objects.all()
		return render(self.request, self.template_name, {'form':form,'text':text,'list':course_list})

	def post(self, request, *args, **kwargs):
		print (request.POST)
		offeredForm = OfferedForm(request.POST)
		if offeredForm.is_valid():
			offeredForm.save()

		new_form = OfferedForm()
		course_list = Course.objects.all()
		return render(request, self.template_name, {'form':new_form,'list':course_list})


class saveCourses(generic.DetailView):

	def fetch_data():
		import os
		cwd = os.getcwd()
		soup = BeautifulSoup(open(cwd + '/kronFrame/coursedata_w2018.txt'),'html.parser')
		rows = soup.find_all('tr')	
		course_data = []
		for row in rows:
		    cols = row.find_all('td')[:4]
		    cols = [ele.text.strip() for ele in cols]
		    cols.append(cols[0][:3]) # append category
		    cols.append("w2018") # append semester
		    if len(course_data) < 15:
		    	cols.append(2)
		    else:
		    	cols.append(3)
		    course_data.append([ele for ele in cols if ele])

		return course_data

	def convert_date_format(time):
		hrs = time.split(":")
		if int(hrs[0]) < 8:
			hrs[0] = str(int(hrs[0]) + 12)
		return ':'.join(hrs)


	def get(self,request):
		"""
		Course Data list format
		# Course ID # Name # Instructor # Timings+Room # Category # Semester # Year #
		"""
		data = saveCourses.fetch_data()
		for course_data in data:
			# print(course_data)
			if(len(course_data) < 7):
				continue
			course, created = Course.objects.get_or_create(cid = course_data[0])
			# print("\n\n" + str(created) + "\n\n")
			if created:
				# print("\n\nINSIDE\n\n\n\n\n\n")				
				course.name = course_data[1]
				course.semester = course_data[5]
				course.year = course_data[6]

				categories_dict = {value: key for key, value in Course.CATEGORIES}
				if course_data[4] not in categories_dict:
					course.category = Course.CATEGORY_OTH
				else:
					course.category = categories_dict[course_data[4]]
				# print(course.category)
				# print("\n\n\n\n\n\n")
				course.save()

			inst, created = Instructor.objects.get_or_create(course=course, name=course_data[2])
			

			timings = course_data[3].replace("\n","-")
			timings = timings.replace("-"," ")
			timings = timings.split(" ")
			t_list = [t.strip() for t in timings if len(t) > 1]
			
			day_dict = {value: key for key, value in Offered.DAY_CHOICES}
			time_dict = {value: key for key, value in Offered.TIME_CHOICES}
			
			if(len(t_list)%4 == 0):
				for i in range(int(len(t_list)/4)):
					# sample ['Mon', '10:00', '11:30', 'C13']
					class_day = day_dict[t_list[i*4 + 0]]

					st_time = saveCourses.convert_date_format(t_list[i*4 + 1])
					start_time = time_dict[st_time]
					
					offered, created = Offered.objects.get_or_create(course=course, class_day=class_day, start_time=start_time)
					if created:
						end_time = saveCourses.convert_date_format(t_list[i*4 + 2])
						offered.end_time = time_dict[end_time]

						offered.areaName = t_list[i*4 + 3]
						offered.save()

		return HttpResponse("Saved!")