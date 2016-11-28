from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse 


class Advisor_Timeslot(models.Model):
    date_time = models.DateTimeField(blank=True)
    advisor = models.CharField(max_length=250) 
    

    def __str__(self):
        return self.advisor  + ' - ' + self.date_time.strftime(" %d - %m - %y , %I : %M %p")
    
    def __add__(self,other):
        return str(self) + other

    def __radd__(self,other):
        return other + str(self)

#session created when a student is assigned to an Advisor_Timeslot

class Session(models.Model):
    timeslot = models.ForeignKey(Advisor_Timeslot,blank=True, on_delete=models.CASCADE)
    student = models.CharField(max_length=250,blank=True)
   
    def get_absolute_url(self):
        return reverse('advisingplus:view_Session', kwargs={'pk':self.pk})

    def __str__(self):
        return self.student + ' - ' + self.timeslot 

    def __add__(self,other):
        return str(self) + other

    def __radd__(self,other):
        return other + str(self)

class Note(models.Model):
    sessionId = models.ForeignKey(Session,blank=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.sessionId + ' - ' +  self.content 

    def __add__(self,other):
        return str(self) + other

    def __radd__(self,other):
        return other + str(self)

class Document(models.Model):
    sessionId = models.ForeignKey(Session, blank=True,  on_delete=models.CASCADE)
    docLink = models.FilePathField
    docType = models.CharField(max_length=10)
    requestReason = models.CharField(max_length=400)
    
    def __str__(self):
        return self.sessionId + ' - ' + self.requestReason 

    def __add__(self,other):
        return str(self) + other

    def __radd__(self,other):
        return other + str(self)

class Student_Feedback(models.Model):   
    sessionId = models.ForeignKey(Session, blank=True, on_delete=models.CASCADE)
    student_feedback = models.CharField(max_length=500)
     
    def __str__(self):
        return str(self.sessionId) 

    def __add__(self,other):
        return str(self) + other

    def __radd__(self,other):
        return other + str(self)
