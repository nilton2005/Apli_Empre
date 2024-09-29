from django.shortcuts import redirect, render
from .models import User, Events, RegisterEvents
# import important libraries
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from .models import Events, RegisterEvents, User
# Create your views here.
def home(request):
    users = User.objects.all()
    events = Events.objects.all()
    context = {'users':users, 'events':events}
    #logic for add register event
    if request.method == 'POST':
        userID = request.POST['user']
        user = User.objects.get(id=userID)
        eventID = request.POST['event']
        event = Events.objects.get(id=eventID)
        register = RegisterEvents(user=user, event=event)
        register.save()
        return redirect('home')
    return render(request, 'home/home.html', context)

def events(request):
    #traer todos los eventos
    events = Events.objects.all()
    registrosID = RegisterEvents.objects.values_list('id', flat=True)
    context = {'events':events, 'registrosID':registrosID}
    for r in registrosID:
        print(r)
    return render(request, 'events/listEvents.html', context)

def addEvent(request):
    if request.method == 'POST':
        title = request.POST['title']
        date = request.POST['date']
        city = request.POST['city']
        artist = request.POST['artist']
        print(title, date, city, artist)
        event = Events(title=title, date=date, city=city, artist=artist)
        event.save() 
        print("-----------addin user --------------")
        return redirect('events')
    return render(request, 'events/addEvents.html')
def editEvent(request, id):
    event = Events.objects.get(id=id)
    context = {'event':event}
    return render(request, 'events/editEvents.html', context)
def deleteEvent(request, id):
    event = Events.objects.get(id=id)
    event.delete()
    return redirect('events')


#CRUD de usuarios

def users(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'users/listUser.html', context)

def addUser(request):
    if request.method == 'POST':
        userName = request.POST['username']
        lastName = request.POST['lastname']
        Imeil = request.POST['email']
        Phone = request.POST['phone']
        print(Phone)
        user = User(username = userName, lastname = lastName, email = Imeil, phone = Phone)
        user.save()
        return redirect('users')
    return render(request, 'users/addUser.html')


#register events
def addRegisterEvent(request):
    if request.method == 'POST':
        user = request.POST['user']
        event = request.POST['event']
        print(user, event)
        register = RegisterEvents(user=user, event=event)
        register.save()
        return redirect('home.html')
    users = User.objects.all()
    events = Events.objects.all()
    context = {'users':users, 'events':events}
    return render(request, 'home/home.html', context)    




def listRecords(request):
    records = RegisterEvents.objects.all()
    for r in records:
        print(r)

    context = {'records':records}
    return render(request, 'records/listRecords.html', context)

# usando el ORM de django
def statistics_view(request):
    now = timezone.now()
    one_month_ago = now - timedelta(days=30) 
    recent_events = Events.objects.filter(date__gte=one_month_ago)
    active_users = User.objects.annotate(event_count=Count('registerevents')).order_by('-event_count')[:5]
    popular_events = Events.objects.annotate(registration_count=Count('registerevents')).order_by('-registration_count')[:5] 
    popular_events_by_city = Events.objects.values('city').annotate(registration_count=Count('registerevents')).order_by('-registration_count')
    users_per_event = RegisterEvents.objects.values('event__title').annotate(user_count=Count('user')).order_by('-user_count')
    context = {
        'recent_events': recent_events,
        'active_users': active_users,
        'popular_events': popular_events,
        'popular_events_by_city': popular_events_by_city,
        'users_per_event': users_per_event,
    }

    return render(request, 'statistics/statistics.html', context)