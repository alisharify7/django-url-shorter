from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.
from linkshorter.models import Urls



def short2original(request, short):
    linkURL = get_object_or_404(Urls, shortURL=short)
    return HttpResponseRedirect(linkURL.originalURL)