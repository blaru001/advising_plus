from django.db import models


class Advisor_Timeslot(models.Model):
    date_time = models.DateTimeField(blank=True)
    advisor = models.CharField(max_length=250) 


#session created when a student is assigned to an Advisor_Timeslot

class Session(models.Model):
    timeslot = models.ForeignKey(Advisor_Timeslot,blank=True, on_delete=models.CASCADE)
    student = models.CharField(max_length=250,blank=True)
    

class Note(models.Model):
    sessionId = models.ForeignKey(Session,blank=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=400, blank=True)


class Document(models.Model):
    sessionId = models.ForeignKey(Session, blank=True,  on_delete=models.CASCADE)
    docLink = models.FilePathField
    docType = models.CharField(max_length=10)
    requestReason = models.CharField(max_length=400)
    
class Student_Feedback(models.Model):   
    sessionId = models.ForeignKey(Session, blank=True, on_delete=models.CASCADE)
    student_feedback = models.CharField(max_length=500)
     
