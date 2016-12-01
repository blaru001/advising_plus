from django.contrib import admin
from .models import Advisor_Timeslot, Session, Note, Document, Student_Feedback, Advisor_Status  

admin.site.register(Advisor_Timeslot)
admin.site.register(Session)
admin.site.register(Note)
admin.site.register(Document)
admin.site.register(Student_Feedback)
admin.site.register(Advisor_Status)
