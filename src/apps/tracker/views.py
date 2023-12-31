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
            return redirect(('/history'))
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
    
    top5_upcycled = dict(sorted(food_counts.items(), key=lambda item: item[1]['upcycled'], reverse=True)[:5])
    top5_thrown = dict(sorted(food_counts.items(), key=lambda item: item[1]['thrown_away'], reverse=True)[:5])
            
    context = {'food_counts': food_counts, 'top5_upcycled':top5_upcycled, 'top5_thrown':top5_thrown}
    return render(request, 'tracker/history.html', context)

# Load index (home) page
def intro(request):

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
    
    top5_upcycled = dict(sorted(food_counts.items(), key=lambda item: item[1]['upcycled'], reverse=True)[:5])
    top5_thrown = dict(sorted(food_counts.items(), key=lambda item: item[1]['thrown_away'], reverse=True)[:5])
            
    context = {'food_counts': food_counts, 'top5_upcycled':top5_upcycled, 'top5_thrown':top5_thrown}
 
    return render(request, 'tracker/index.html', context)

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
            return redirect('/add')
    context = {'form':form}
    return render(request, 'tracker/add.html', context)


