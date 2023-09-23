from django.shortcuts import render
from apps.tracker.models import FoodAdvice

# Create your views here
def food_tracker(request):
    food_tracker = FoodAdvice.objects.all()
    return render(request, 'tracker/tracker.html', {'food_tracker': food_tracker})


# Select and return food information
def search_food(request):
    query = request.GET.get('food_name')
    food_items = FoodAdvice.objects(filter(name__icontains=query))
    return render(request, 'tracker/tracker.html', {'food_items':food_items})

def food(request, pk):
    # Find the food by ID
    food = FoodAdvice.objects.filter(id=pk)
    # Get data for specific food item
    food_advice = food.all()
    context = {'food':food, 'food_advice':food_advice}
    return render(request, 'tracker/food.html', context)

