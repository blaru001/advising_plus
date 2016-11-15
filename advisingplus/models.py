from django.db import models


class Session(models.Model):
    student = models.CharField(max_length=250)

class Notes(models.Model):
    sessionId = models.ForeignKey(Session, on_delete=models.CASCADE)
    
class Schedule(models.Model):
    sessionId = models.ForeignKey(Session, on_delete=models.CASCADE)
    StartTime = models.TimeField
    date = models.DateField
    advisor = models.CharField(max_length=250)

class Documents(models.Model):
    sessionId = models.ForeignKey(Session, on_delete=models.CASCADE)
    docLink = models.FilePathField
    docType = models.CharField(max_length=10)
    requestReason = models.CharField(max_length=400)
    
class Student_Feedback(models.Model):   
    sessionId = models.ForeignKey(Session, on_delete=models.CASCADE)
    student_feedback = models.CharField(max_length=500)
     
