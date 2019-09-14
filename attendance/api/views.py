from rest_framework import generics
from ..models import Schedule, Attendance, Students
from .serializers import ScheduleSerializer
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.views import APIView
import face_recognition
from PIL import Image
import numpy as np

class DayScheduleView (generics.ListAPIView) :

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class PostAttendance (APIView) :

    def post (self, request) :
        students = Students.objects.all()
        s = request.data['unknown_encoding']
        s = s[1:-2]
        l = list(map(float,s.split(',')))
        unknown_encoding = np.array(l)
        for i in students :
            img = face_recognition.load_image_file(i.photo_id)
            img_face = face_recognition.face_locations(img)
            print (i.name)
            top, right, bottom, left = img_face[0]
            known_image = img[top:bottom, left:right]
            biden_encoding = face_recognition.face_encodings(known_image)[0]
            results = face_recognition.compare_faces([biden_encoding],unknown_encoding)
            print(results)
            if (results[0] == True) :
                matched_person = i.name
        return Response({"message":"{} is marked present".format(matched_person)})

