from django.db import models


class Advisor_Timeslot(models.Model):
   # StartTime = models.TimeField
   # date = models.DateField
    advisor = models.CharField(max_length=250)

#session created when a student is assigned to an Advisor_Timeslot
class Session(models.Model):
    timeslot = models.ForeignKey(Advisor_Timeslot, on_delete=models.CASCADE)
    student = models.CharField(max_length=250)
    
    def __str__(self):
        return self.student


class Notes(models.Model):
    sessionId = models.ForeignKey(Session, on_delete=models.CASCADE)
    content = models.CharField(max_length=400, blank=True)


class Documents(models.Model):
    sessionId = models.ForeignKey(Session, on_delete=models.CASCADE)
    docLink = models.FilePathField
    docType = models.CharField(max_length=10)
    requestReason = models.CharField(max_length=400)
    
class Student_Feedback(models.Model):   
    sessionId = models.ForeignKey(Session, on_delete=models.CASCADE)
    student_feedback = models.CharField(max_length=500)
     
