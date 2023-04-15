from django.shortcuts import render


dogs = [
  {'name': 'Theo', 'breed': 'mix', 'description': 'black and white wiggle butt', 'age': 5},
  {'name': 'Evergreen', 'breed': 'German Shepard, Australian Cattle Dog', 'description': 'anxious, but hard working and loyal', 'age': 2},
]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {
    'dogs': dogs
    })