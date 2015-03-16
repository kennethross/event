from django.conf.urls import patterns, include, url
from django.contrib import admin
from submit import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.abcdisplay, name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^submit/', include('submit.urls')),
	url(r'^abcdisplay/$','submit.views.abcdisplay'),
	url(r'^batchdata/$','submit.views.batchdata'),
	url(r'^uploadfile/$', 'submit.views.uploadfile', name ='name'),
	url(r'^displayupload/$', 'submit.views.displayupload'),
	url(r'^admin/', include(admin.site.urls)),

	
	
)

    
    




