# Generated by Django 4.2.1 on 2023-05-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0002_alter_groupstudent_name_alter_student_group_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='tutor',
        ),
        migrations.AddField(
            model_name='schedule',
            name='tutor',
            field=models.ManyToManyField(to='college_app.tutor', verbose_name='Преподаватель'),
        ),
    ]
