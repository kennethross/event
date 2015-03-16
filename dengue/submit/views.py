from django.http import HttpResponse
from django.template import RequestContext, loader
from submit.models import ViewSubmitData
from submit.models import ViewBatchList
from submit.forms import FileForm
from submit.models import Document	
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.shortcuts import render_to_response
import csv
from submit.models import Invite
from django.conf import settings

def abcdisplay(request):
	posts = ViewSubmitData.objects.all()
	print posts
	return render(request, 'submit/index.html', {"posts": posts})
	#return render_to_response('submit/index.html', {"posts": posts})
	
def batchdata (request):
    batch=ViewBatchList.objects.all()
    print batch 
	#return render(request, 'submit/view.html', {"batch": batch})
    return render_to_response('submit/view.html', {"batch": batch})

def displayupload(request):
	uploaddata=ViewBatchList.objects.all()
	print uploaddata
	return render_to_response('submit/see.html', {"uploaddata": uploaddata})

def uploadfile(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FileForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            csv_path = request.FILES['docfile']
            ##print csv_path.read()
            csv_reader = csv.DictReader(csv_path)
            for row in csv_reader:
			
				##if len(row) == 2:
						obj = Invite.objects.create(
						name=row['name'],
						date=row['date']
						)
						print obj
		 	
			


				##print csv_path.size
		
			
            
            return HttpResponseRedirect('/displayupload/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FileForm()

    return render(request, 'submit/name.html', {'form': form})







	
