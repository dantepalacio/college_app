from django.db import models
from django.contrib.auth.models import User, AbstractUser, Permission
from django.core.validators import MaxValueValidator, MinValueValidator

class News(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField()
	image = models.ImageField(upload_to="news", null=True, blank=True, width_field="")
	datetime = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Жаңалықтар'
		verbose_name_plural = 'Жаңалықтар'

class ClassTime(models.Model):
	time = models.CharField('Время занятий', blank=True, max_length=200)

	class Meta:
		verbose_name = 'Сабақ уақыты'
		verbose_name_plural = 'Сабақ уақыты'

	def __str__(self):
		return self.time

class Day(models.Model):
	name = models.CharField('', max_length=200)

	class Meta:
		verbose_name = 'Аптаның күні'
		verbose_name_plural = 'Аптаның күні'

	def __str__(self):
		return self.name
	

class Subject(models.Model):
	name = models.CharField('', max_length=200, null=True, blank=True)

	class Meta:
		verbose_name = 'Сабақ'
		verbose_name_plural = 'Сабақтар'

	def __str__(self):
		return self.name


class Tutor(models.Model):
	fullname = models.CharField('', max_length=200)

	class Meta:
		verbose_name = 'Оқытушы'
		verbose_name_plural = 'Оқытушылар'

	def __str__(self):
		return self.fullname

class GroupStudent(models.Model):
	name = models.CharField('Код группы', max_length=200, default='IS-21-3', null=True, blank=True)

	class Meta:
		verbose_name = 'Топ'
		verbose_name_plural = 'Топтар'

	def __str__(self):
		return self.name
	

class Student(AbstractUser):
	group_student = models.ForeignKey(GroupStudent, on_delete=models.CASCADE, null=True, blank=True, related_name='students')

	class Meta:
		verbose_name = 'Студент'
		verbose_name_plural = 'Студенттер'


class Cabinet(models.Model):
	cab = models.PositiveIntegerField()

	def __str__(self):
		return str(self.cab)
	
	class Meta:
		verbose_name = 'Кабинет'
		verbose_name_plural = 'Кабинеттер'


class SubjectTutor(models.Model):
	tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True, blank=True)
	subject  = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
	
	class Meta:
		verbose_name = 'Оқытушының мамандануы'
		verbose_name_plural = 'Оқытушылардың мамандануы'

	def __str__(self):
		return f'{self.tutor} {self.subject}'
  

class Schedule(models.Model):
	day = models.ForeignKey(Day, on_delete=models.CASCADE)
	
	group = models.ForeignKey(GroupStudent, on_delete=models.CASCADE, null=True, blank=True)

	subject = models.ForeignKey(Subject, verbose_name='Предметы', on_delete=models.CASCADE, null=True, blank=True)

	time = models.ForeignKey(ClassTime, verbose_name='Время', on_delete=models.CASCADE, null=True, blank=True)

	tutor = models.ForeignKey(Tutor, verbose_name='Преподаватель', on_delete=models.CASCADE, null=True, blank=True)

	cabinet = models.ForeignKey(Cabinet, verbose_name='Кабинет', on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		verbose_name = 'Кесте'
		verbose_name_plural = 'Кестелер'

	def __str__(self):
		return f'{self.group} {self.day}'

class Grade(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	
	grade = models.SmallIntegerField(default=0,
									 validators=[
											MaxValueValidator(5),
											MinValueValidator(1)
									 ])
	date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	class Meta:
		verbose_name = 'Баға'
		verbose_name_plural = 'Бағалар'

	def __str__(self):
		return f'{self.student}, {self.subject}, {self.grade}'