from django.shortcuts import HttpResponse

from .components.index import index_page, not_found_page


def index(request):
    return HttpResponse(index_page().render())


def not_found(request):
    return HttpResponse(not_found_page().render())