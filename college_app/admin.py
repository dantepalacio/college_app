from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group as GR



# admin.site.unregister(User)
admin.site.unregister(GR)


# class StudentAdmin(admin.ModelAdmin):

#     # list_display = ('first_name', 'last_name', 'group')

#     fields = ('username', 'password', 'first_name', 'last_name','group_student')
    

#     def save_model(self, request, obj, form, change):
#         # if 'password' in form.cleaned_data:
#         # if obj.password:
#         #     obj.set_password(form.cleaned_data['password'])  # Хэшируем пароль


#         password = form.cleaned_data['password']
#         if password:
#                 obj.set_password(password)


#         super().save_model(request, obj, form, change)



class StudentAdmin(UserAdmin):
    
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'group_student')}),
    )
    
    add_fieldsets = (
        (None, {
                    'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'group_student'),
                }),
    )



admin.site.register(Student, StudentAdmin)
admin.site.register(News)
admin.site.register(Schedule)
admin.site.register(GroupStudent)
admin.site.register(Day)
admin.site.register(Subject)
admin.site.register(ClassTime)
admin.site.register(Tutor)
admin.site.register(Cabinet)
admin.site.register(SubjectTutor)

admin.site.register(Grade)




