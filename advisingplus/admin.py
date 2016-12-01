from django.contrib import admin
from .models import Timeslot, Session, Note, Document, Feedback, Status  

admin.site.register(Timeslot)
admin.site.register(Session)
admin.site.register(Note)
admin.site.register(Document)
admin.site.register(Feedback)
admin.site.register(Status)
