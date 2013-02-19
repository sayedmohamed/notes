from django.conf.urls import patterns, include, url
from models import Note

notes = Note.objects.all()

urlpatterns = patterns(
	'',
	url(r'^$', 'django.views.generic.list_detail.object_list',
		dict(queryset = notes)),
	url(r'^note/(?P<slug>[-\w]+)/$','django.views.generic.list_detail.object_detail',
		dict(queryset = notes, slug_field='slug')),
	url(r'^create/$', 'notes.views.create_note'),
	url(r'^note/(?P<slug>[-\w]+)/update/$','notes.views.update_note'),
	)