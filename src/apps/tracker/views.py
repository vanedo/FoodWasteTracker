from django.db import models
from django.db.models import Count
from django.shortcuts import render, redirect
from apps.tracker.models import FoodAdvice, FoodHistory
from apps.tracker.forms import FoodHistoryForm, ContributeDataForm
from django.http import JsonResponse

# Create your views here
def food_tracker(request):
    food_tracker = FoodAdvice.objects.all()
    return render(request, 'tracker/tracker.html', {'food_tracker': food_tracker})

def food(request, pk):
    # Find the food by ID
    food = FoodAdvice.objects.filter(id=pk)
    # Get data for specific food item
    food_advice = food.all()
    # Save ID to prefill field
    initial_data = {
        'food':pk
    }
    # Get responses
    form = FoodHistoryForm(initial=initial_data)
    # Save reponses
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form=FoodHistoryForm(request.POST)
        print('Form is valid:', form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/food-tracker')
    context = {'food':food, 'food_advice':food_advice, 'form':form}
    return render(request, 'tracker/food.html', context)

def history(request):
    foodhistory = FoodHistory.objects.all()
    # Create empty dictionary to capture data
    food_counts = {}
    # Loop through list and count for each time a value appears
    for item in foodhistory:
        food_name = item.food
        eaten = item.eaten
        if food_name not in food_counts:
            food_counts[food_name] = {'thrown_away': 0, 'upcycled': 0}
        if eaten == 'thrown_away':
            food_counts[food_name]['thrown_away'] += 1
        elif eaten == 'upcycled':
            food_counts[food_name]['upcycled'] += 1
    return render(request, 'tracker/history.html', {'food_counts': food_counts})

# return top 5 upcycled items as a list
def top_upcycled(request):
    #data = FoodHistory.objects.filter(eaten='Upcycle')[:5]
    #data = FoodHistory.objects.filter(eaten='Upcycle').values('name').annotate(count=models.Count('eaten')).order_by('-count')[:5]
    labels = []
    data = []
    for entry in data:
        labels.append(entry['name'])
        data.append(entry['eaten'])
    return render(request, 'tracker/history.html', {'up_labels': labels, 'up_counts': data})

# Load index (home) page
def intro(request):

    return render(request, 'tracker/index.html')

# Redirect to index page when landing on site
def homepage(request):
    return redirect(('/index'))

# Load form to add in data 
def add(request):
    # Get responses
    form = ContributeDataForm()
    # Save reponses
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form=ContributeDataForm(request.POST)

        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'tracker/add.html', context)


