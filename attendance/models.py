from django.db import models

class Batch (models.Model) :
    identifier = models.CharField(max_length=50)
    strength = models.IntegerField()

    def __str__(self) :
        return "{}".format(self.identifier)
        
class Students (models.Model) :
    name = models.CharField(max_length=50)
    reg_no = models.CharField(max_length=50)
    batch = models.ForeignKey(to=Batch, on_delete=models.CASCADE)
    photo_id = models.ImageField(upload_to='users/')

    def __str__ (self) :
        return "Student : {} - {}".format(self.name, self.reg_no)

class Venue (models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self) :
        return "{}".format(self.name)

class Schedule(models.Model) :
    DAY_CHOICES = (
        ('monday','Monday'),
        ('tuesday','Tuesday'),
        ('wednesday','Wednesday'),
        ('thursday','Thursday'),
        ('friday','Friday'),
        ('saturday','Saturday'),
        ('sunday','Sunday')
    )
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    venue = models.ForeignKey(to = Venue, on_delete=models.CASCADE)
    batch = models.ForeignKey(to=Batch, on_delete=models.CASCADE)
    timing = models.TimeField() 
    def __str__ (self) :
        return "Schedule for - {}".format(self.day)

class Attendance(models.Model) :
    STATUS_CHOICES = (
        ('present','Present'),
        ('absent','Absent')
    )
    student = models.ForeignKey(to=Students, on_delete=models.CASCADE)   
    batch = models.ForeignKey(to=Batch, on_delete=models.CASCADE)
    venue = models.ForeignKey(to=Venue, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)