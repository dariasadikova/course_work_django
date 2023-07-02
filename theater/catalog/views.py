from django.shortcuts import render
from django.views import generic    
from .models import Play, Actor, Ticket, Genre, Viewer, Review, Booking
# Create your views here.

def index(request):
    
    num_plays=Play.objects.all().count()
    num_actors=Actor.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_plays':num_plays,'num_actors':num_actors},
    )
    
from .forms import AddPlayForm
   
def add_play(request):
  
    if request.method == 'POST':
        form = AddPlayForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('plays')
            except:
                form.add_error(None, "Ошибка добавления спектакля")
    else:
        form = AddPlayForm(request.POST)


    form = AddPlayForm()
  
    return render(
        request,
        'add_play.html',
        context={'form':form},
    )
  

class PlayListView(generic.ListView):
    model = Play
    paginate_by = 5

class PlayDetailView(generic.DetailView):
    model = Play

class ActorListView(generic.ListView):
    model = Actor
    paginate_by = 5

class ActorDetailView(generic.DetailView):
    model = Actor
