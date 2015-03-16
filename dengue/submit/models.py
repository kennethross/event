from django.db import models
import datetime

# Create your models here.
class Document(models.Model):
    docfile = models.FileField(upload_to='media/%Y/%m/%d')
 



   

class Insertdata(models.Model):
	event_name = models.CharField(max_length=200)
	event_date = models.DateTimeField('Event Date')
	event_place =models.CharField(max_length=200)
 
class Invite(models.Model):
    name = models.CharField(max_length=500)
    date = models.CharField(max_length=500)

class ViewSubmitData(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=500)
    event_date = models.CharField(max_length=500)
    event_place =models.CharField(max_length=200)
 
    

    class Meta:
		db_table=u'Submit_Insertdata'

    def __unicode__(self):
        return u"%d %s %s" % (self.pk, self.event_name, self.event_place)

class ViewBatchList(models.Model):
		id = models.AutoField(primary_key=True)
		name = models.CharField(max_length=500)
		date= models.CharField(max_length=500)
	
		class Meta:
			db_table=u'submit_invite'

		def __unicode__(self):
			return u"%d %s %s" % (self.pk, self.name, self.date)	
	
		

		





  
	

   
