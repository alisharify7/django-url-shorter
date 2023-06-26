from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from linkshorter.models import Urls



def short2original(request, short):
    """
    This view take a shorturl and check in db
    if found shortlink then redirect user to orginal link
    """
    linkURL = get_object_or_404(Urls, shortURL=short)
    return HttpResponseRedirect(linkURL.originalURL)