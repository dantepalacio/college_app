from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from college_app import models
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Avg
from django.http import HttpResponse
from django import template
from django.shortcuts import get_object_or_404


register = template.Library()

@register.filter
def get_previous(value, index):
	if index > 0 and index < len(value):
		return value[index - 1]
	return None

def schedule_view(request):
	group_id = request.user.group_student_id
	print('FSDFPSJHDSIJDSD ', group_id)

	group = models.GroupStudent.objects.filter(id=group_id)
	lessons = models.Schedule.objects.filter(group_id=group_id)
	days = models.Day.objects.all()
	context = {'group': group, 'lessons': lessons, 'get_previous': get_previous, 'days':days}
	print(context)
	return render(request, 'schedule/schedule.html', context)

class News(ListView):
	model = models.News
	template_name = 'news.html'
	context_object_name = 'news'
		
	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.order_by('-id')

class DetailNews(LoginRequiredMixin, DetailView):
	model = models.News
	template_name = 'detail_news.html'
	context_object_name = 'news'


class CustomLoginView(LoginView):
	template_name = 'auth/login.html'
	success_url = reverse_lazy('news_page')

	def get_success_url(self):
		return self.success_url

class CustomLogoutView(LoginRequiredMixin, LogoutView):
	template_name = 'auth/logout.html'
	next_page = reverse_lazy('news_page')
		

def grade_view(request):
	user_id = request.user.id
	grades = models.Grade.objects.filter(student_id = user_id)
	print(grades)
	average = models.Grade.objects.filter(student_id=user_id).values('subject').annotate(avg_grade=Avg('grade'))


	subject_ids = [entry['subject'] for entry in average]
	subjects = models.Subject.objects.filter(id__in=subject_ids)
	subject_names = {subject.id: subject.name for subject in subjects}
	for entry in average:
		entry['subject'] = subject_names[entry['subject']]

	avgs = [entry['avg_grade'] for entry in average]

	if len(avgs) > 0:
		gpa = sum(avgs) / len(avgs)
		print('ASDOJSHDIJSD',gpa)
	else:
		gpa = 0

	student_info = get_object_or_404(models.Student, id=user_id)



	print('sdfgsdfgsdfhsdhsdfg',student_info)

	context = {'grades':grades, 'average': average, 'gpa': gpa, 'student_info':student_info}
	return render(request, 'my_grades.html', context)




def download_grades(request):
	user_id = request.user.id
	grades = models.Grade.objects.filter(student_id=user_id)

	average = models.Grade.objects.filter(student_id=user_id).values('subject').annotate(avg_grade=Avg('grade'))
	subject_ids = [entry['subject'] for entry in average]
	subjects = models.Subject.objects.filter(id__in=subject_ids)
	subject_names = {subject.id: subject.name for subject in subjects}
	for entry in average:
		entry['subject'] = subject_names[entry['subject']]

	avgs = [entry['avg_grade'] for entry in average]

	student_info = get_object_or_404(models.Student, id=user_id)

	if len(avgs) > 0:
		gpa = sum(avgs) / len(avgs)
		print('ASDOJSHDIJSD',gpa)
	else:
		gpa = 0

	content = f"{student_info.last_name} {student_info.first_name} бағалары\n\n"
	for grade in grades:
		content += f"{grade.subject} - {grade.grade}\n"
	content += f"\nОрташа бағалар:\n"
	for entry in average:
		content += f"{entry['subject']} - {entry['avg_grade']}\n"
	content += f"\nGPA: {round(gpa, 2)}\n"

	response = HttpResponse(content, content_type='text/plain')
	response['Content-Disposition'] = f'attachment; filename="grades.txt"'
	return response