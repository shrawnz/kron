from django.contrib import admin

from .models import Course, Offered, CallSign

class OfferedInline(admin.TabularInline):
	model = Offered
	extra = 0

class CoursesAdmin(admin.ModelAdmin):
	inlines = [OfferedInline]
	list_display = ('name', 'acronym')
# Register your models here.
admin.site.register(Course, CoursesAdmin)

admin.site.register(CallSign)