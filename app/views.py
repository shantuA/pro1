from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Rohith(request):
    return HttpResponse("<h1><center>Rohit Gurunath Sharma🏏<center><h1> <h6>Sharma is known for his timing, elegance, six-hitting abilities and leadership skills."
                         " Sharma holds several batting records which famously include most sixes in international cricket,"
                         "[a] most double centuries in ODI cricket (3), most centuries at Cricket World Cups (7) and"
                          " joint most hundreds in Twenty20 Internationals (5)<h6>")

def Virat(request):
    return HttpResponse("<h1><center>Virat Kohli🏏<center><h1> <h6>Kohli is widely regarded as one of the greatest batsmen of all time.He holds the record as the"
                         "highest run-scorer in IPL, ranks second in T20I, third in ODI, and stands as the fourth-highest in international cricket<h6>")