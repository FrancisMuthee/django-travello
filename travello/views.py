from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    """
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City that rocks'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Maasai Mara'
    dest2.desc = 'Wildabeast'
    dest2.img = 'destination_2.jpg'
    dest2.price = 1000
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'GNP'
    dest3.desc = 'Nature smoothing'
    dest3.img = 'destination_3.jpg'
    dest3.price = 1500
    dest3.offer = False
    """
    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})
