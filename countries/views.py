from django.shortcuts import render
from .models import Country
from django.views.generic import ListView, DetailView
import random
# Create your views here.

def handler404(request, exception=None):
    return render(request, 'countries/404.html')

def game(request):
    random_idx = random.randint(0, Country.objects.count() - 1)
    random_object = Country.objects.all()[random_idx]
    context = {
        'country': random_object
    }
    return render(request, 'countries/game.html',context)

def gameanswer(request):
    random_idx = random.randint(0, Country.objects.count() - 1)
    random_object = Country.objects.all()[random_idx]
    guess=request.GET.get("guess")
    answer=request.GET.get("answer")
    print(type(guess))
    context = {
        'guess':guess,
        'answer':answer,
        'country': random_object
    }
    print(context)
    return render(request, 'countries/gameanswer.html',context)


def home(request):

    return render(request, 'countries/home.html')

class SillyCountryListView(ListView):
    model=Country
    template_name='countries/sillyhome.html'

class CountryListView(ListView):
    model=Country


def info(request):
    return render(request,'countries/info.html')

class CountryDetailView(DetailView):
    model=Country

class SearchCountryListView(ListView):
    model=Country
    template_name='countries/search.html'
    def get_queryset(self):
        queryset = Country.objects.all()
        
        queryset=queryset.filter(name__icontains=self.request.GET.get("q"))
        return queryset