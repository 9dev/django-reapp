from django.http.request import HttpResponse


def dummy(request):
	return HttpResponse('DummyResponse')

