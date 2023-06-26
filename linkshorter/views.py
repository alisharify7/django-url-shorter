from django.shortcuts import render, reverse

# Create your views here.
from .models import Urls
from .utils import generate_unique_short_link


def index(request):
    """Base Index view"""
    context = {}
    return render(request, "linkshorter/index.html", context=context)



def ConvertUrl2Short(request):
    if request.method == "POST":
        context = {}
        url = request.POST.get("url", None)
        if not url:
            context["alert"] = "invalid url"
            context["category"] = "danger"
            return render(request, "linkshorter/index.html", context=context)
        newURL = Urls()
        newURL.originalURL = url
        newURL.shortURL = generate_unique_short_link()
        newURL.save()
        context["alert"] = "short link created successfully"
        context["category"] = "success"
        context["link"] = newURL.shortURL
        return render(request, "linkshorter/index.html", context=context)

