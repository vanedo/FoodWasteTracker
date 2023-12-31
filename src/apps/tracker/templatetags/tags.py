from apps.tracker.models import FoodHistory
from django import template

register = template.Library()

@register.simple_tag
def metric_contributions(request):
    upcycled_count = FoodHistory.objects.filter(eaten='upcycled').count()
    thrown_count = FoodHistory.objects.filter(eaten='thrown_away').count()
    contributions = upcycled_count + thrown_count # contributions to website, not eg donations 

    return contributions

@register.simple_tag
def metric_red_emissions(request):
    upcycled_count = FoodHistory.objects.filter(eaten='upcycled').count()
    red_emissions = 0.5 * 2.5 * upcycled_count # assume 0.5kg per item, 2.5kg CO2 saved per kg

    return red_emissions

@register.simple_tag
def metric_items_saved(request):
    upcycled_count = FoodHistory.objects.filter(eaten='upcycled').count()

    return upcycled_count
