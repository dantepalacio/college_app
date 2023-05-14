from college_app import models
from django.shortcuts import get_object_or_404

def student(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        group_id = request.user.group_student_id
        student_info = get_object_or_404(models.Student, id=user_id)
        group = models.GroupStudent.objects.filter(id=group_id)
        context = {'student_info': student_info, 'groups': group}
    else:
        context = {}
    
    return context