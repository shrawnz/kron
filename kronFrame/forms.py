from django import forms
from django.forms.models import ModelForm, ModelChoiceField
from kronFrame.models import *
from django.forms.widgets import Textarea, RadioSelect, HiddenInput,\
    CheckboxInput, TextInput, Select, URLInput, ClearableFileInput,\
    SelectDateWidget, NumberInput
from django.forms.fields import IntegerField, CharField, URLField, DateField
from django.contrib.admin.helpers import checkbox


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = [ 'name', 'course_id', 'acronym', 'credits', 'category', 'choice_type','semester']
        
        labels = {
            'name':('Name'),
			'course_id':('ID'),
			'acrnoym':('Acronym'),
			'credits':('Credits'),
			'category':('Category'),
			'choice_type':('Type'),
            'semester':('Semester')
        }

        widgets = {
             'name': TextInput(),
             'course_id': TextInput(),
             'acronym': TextInput(),
             'credits': RadioSelect(),
             'category': Select(), 
             'choice_type': RadioSelect(),
             'semester' : TextInput()
        }

