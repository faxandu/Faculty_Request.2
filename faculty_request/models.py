from django.db import models
from django.contrib.auth.models import User



ROOM='Room'
EQUIPMENT= 'Equipment'
CONFIGURE='Configure'
LABS='Labs'
OTHER='Other'
PENDING='Pending'
APPROVED='Approved'
DELEGATED='Delegated'
COMPLETED='Completed'


request_type= (
    (ROOM,'Room'),
    (EQUIPMENT, 'Equipment'),
    (CONFIGURE,'Configure'),
    (LABS,'Labs'),
    (OTHER,'Other'),
)
request_status=(
    (PENDING,'Pending'),
    (APPROVED,'Approved'),
    (DELEGATED,'Delegated'),
    (COMPLETED,'Completed'),
)
class Requests (models.Model):
    faculty_Name=models.ForeignKey(User,related_name='+')
    labtech_Name=models.ForeignKey(User,related_name='+',blank=True,null=True,)
    uploaded= models.TextField(max_length=100, blank=True,)
    subject=models.CharField(max_length=100)
    description=models.TextField()
    issued_date=models.DateTimeField(auto_now_add=True)
    due_date=models.DateField()
    request_Type=models.CharField(max_length=20, choices=request_type, default=OTHER)
    request_status=models.CharField(max_length=20,choices=request_status,default=PENDING)     

    def __unicode__(self):
        return unicode(self.subject)

    def to_dict(self):
        return {
            'faculty_Name': self.faculty_Name.username,
            'labtech_Name': self.labtech_Name.username,
            'subject': self.subject,
            'description': self.description,
            'upload': self.uploaded,
            'issued_date': unicode(self.issued_date),
            'due_date': unicode(self.due_date),
            'request_status': self.request_status,
            'pk': self.pk,
        }
            
# Create your models here.
