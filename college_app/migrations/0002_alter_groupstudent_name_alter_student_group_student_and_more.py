# Generated by Django 4.2.1 on 2023-05-13 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('college_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupstudent',
            name='name',
            field=models.CharField(blank=True, default='IS-21-3', max_length=200, null=True, verbose_name='Код группы'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group_student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='college_app.groupstudent'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
