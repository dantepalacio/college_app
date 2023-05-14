# Generated by Django 4.2.1 on 2023-05-13 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0006_remove_schedule_subject_remove_schedule_tutor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjecttutor',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='subjecttutor',
            name='tutor',
        ),
        migrations.AddField(
            model_name='subjecttutor',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='college_app.subject'),
        ),
        migrations.AddField(
            model_name='subjecttutor',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='college_app.tutor'),
        ),
    ]