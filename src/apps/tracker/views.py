from django.shortcuts import render
from apps.tracker.models import FoodAdvice, FoodHistory

# Create your views here
def food_tracker(request):
    food_tracker = FoodAdvice.objects.all()
    return render(request, 'tracker/tracker.html', {'food_tracker': food_tracker})


def food(request, pk):
    # Find the food by ID
    food = FoodAdvice.objects.filter(id=pk)
    # Get data for specific food item
    food_advice = food.all()
    context = {'food':food, 'food_advice':food_advice}
    return render(request, 'tracker/food.html', context)

def history(request):
    foodhistory = FoodHistory.objects.all()
    # Create empty dictionary
    food_counts = {}
    # Loop through list
    for item in foodhistory:
        food_name = item.name
        eaten = item.eaten
        if food_name not in food_counts:
            food_counts[food_name] = {'yes': 0, 'no': 0}
        if eaten == 'Yes':
            food_counts[food_name]['yes'] += 1
        elif eaten == 'No':
            food_counts[food_name]['no'] += 1
    return render(request, 'tracker/history.html', {'food_counts': food_counts})

