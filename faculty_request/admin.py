from django.contrib import admin
from faculty_request.models import Requests



class request_admin(admin.ModelAdmin):
	list_display = ('faculty_Name','request_Type','subject','issued_date','due_date','labtech_Name','request_status',)
	list_filter=('faculty_Name',)
	search_field=['subject','faculty_Name','labtech_Name',]


admin.site.register(Requests,request_admin )
      
