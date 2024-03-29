from django.db import models 
from datetime import datetime
from django.core.urlresolvers import reverse 
from django.contrib.auth.models import User 



class Status(models.Model):
    advisor_available = models.BooleanField() 
    advisor = models.ForeignKey(User, unique=True)
    
    def get_absolute_url(self):
        return reverse('advisingplus:status-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.advisor)

class Timeslot(models.Model):
    date_time = models.DateTimeField(blank=True)
    advisor = models.ForeignKey(User)
    
    def get_absolute_url(self):
        return reverse('advisingplus:timeslot-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return 'Advisor: ' + str( self.advisor)  + ' - ' + self.date_time.strftime("Date: %d - %m - %y Time: %I : %M %p")
    
    def __add__(self,other):
        return str(self) + other

    def __radd__(self,other):
        return other + str(self)

#session created when a student is assigned to an Advisor_Timeslot

class Session(models.Model):
    timeslot = models.ForeignKey(Timeslot,blank=True, on_delete=models.CASCADE)
    student = models.ForeignKey(User)
   
    def get_absolute_url(self):
        return reverse('advisingplus:session-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.student) + ' - ' + self.timeslot 

    def __add__(self,other):
        return str(self) + other

    def __radd__(self,other):
        return other + str(self)
    
    def getdocs(self):
        return  self.document_set.all() 

class Note(models.Model):
    sessionId = models.ForeignKey(Session,blank=True)
    content = models.CharField(max_length=400, blank=True)

    def get_absolute_url(self):
        return reverse('advisingplus:note-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.sessionId + ' - ' +  self.content 

    def __add__(self,other):
        return str(self) + other

    def __radd__(self,other):
        return other + str(self)

class Document(models.Model):
    sessionId = models.ForeignKey(Session, blank=True )
    doc = models.FileField(blank = True)
    docname = models.CharField(blank = True ,max_length=100)
    requestReason = models.CharField(max_length=400)


    def get_absolute_url(self):
        return reverse('advisingplus:document-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.sessionId + ' - ' + self.requestReason 

    def __add__(self,other):
        return str(self) + other

    def __radd__(self,other):
        return other + str(self)
    
    def getUrl(self):
        return self.doc.url

class Feedback(models.Model):   
    sessionId = models.ForeignKey(Session, blank=True, )
    student_feedback = models.CharField(max_length=500)
     
    def get_absolute_url(self):
        return reverse('advisingplus:feedback-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.sessionId) 

    def __add__(self,other):
        return str(self) + other

    def __radd__(self,other):
        return other + str(self)
