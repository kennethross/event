from django.contrib import admin
from submit.models import Insertdata
from submit.models import Invite
from submit.models import ViewSubmitData


class Display(admin.ModelAdmin):
    list_display = ("name","date")
class DisplayData(admin.ModelAdmin):
    list_display=("id","event_name","event_date")
	




admin.site.register(Insertdata)
admin.site.register(Invite,Display)
admin.site.register(ViewSubmitData,DisplayData)





# Register your models here.



