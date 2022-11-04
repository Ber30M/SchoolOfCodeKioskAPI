from multiprocessing import context
from django.shortcuts import render

# we gonna define methodes that gonna help us to render html code


def home(request):
    context={}
    return render(request, "api/home.html", context)

# let's run the server