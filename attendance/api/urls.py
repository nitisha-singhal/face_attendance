from django.urls import	path 
from . import views

app_name = 'attendance'

urlpatterns	=	[				
    path('schedule/', views.DayScheduleView.as_view(), name='subject_list'),
    path('attendcheck/', views.PostAttendance.as_view(), name='post_attendance')
    ]
