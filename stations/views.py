from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_stations = []
    with open ('data-398-2018-08-30.csv', encoding="utf-8") as file:
        CONTENT = csv.DictReader(file)
        for row in CONTENT:
            bus_stations.append(row)
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'page': page
    }
    return render(request, 'stations/index.html', context)
