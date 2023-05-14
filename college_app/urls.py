from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.News.as_view(), name='news_page'),
    path('news/<int:pk>/', views.DetailNews.as_view(), name='news_detail_page'),
    path('my_schedule/', views.schedule_view, name='my_schedule'),
    path('my_grade/', views.grade_view, name='my_grade'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('download_grades/', views.download_grades, name='download_grades'),

]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)