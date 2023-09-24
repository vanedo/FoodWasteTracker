from django.db import models


# Create your models here.

class FoodAdvice(models.Model):
    RECOMMEND = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    food_id = models.CharField(max_length=10)
    category_name = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)
    name_subtitle = models.CharField(max_length=100, null=True)
    keywords = models.CharField(max_length=300, null=True)
    pantry_max_days = models.CharField(max_length=100)
    pantry_tips = models.CharField(max_length=300)
    fridge_needed = models.CharField(max_length=5, null=True, choices=RECOMMEND)
    refrigerate_max_days = models.PositiveIntegerField(null=True)
    refrigerate_ao_max_days = models.PositiveIntegerField(null=True)
    refrigerate_tips = models.CharField(max_length=300)    
    freeze_recommended = models.CharField(max_length=5, null=True, choices=RECOMMEND)
    compost = models.CharField(max_length=10)
    food_waste_index = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model to capture action on the food.html page
class FoodAction(models.Model):
    ACTION = (
        ('ThrownAway','ThrownAway'),
        ('ThrownAway','Upcycled')
        )
    food_id = models.CharField(max_length=10)
    action_type = models.CharField(max_length=10, choices=ACTION)
    # likes = models.ManytoManyField(FoodAdvice)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.food_id)
    
class FoodHistory(models.Model):
    ACTION = (
        ('thrown_away', 'Throw it away'),
        ('upcycled', 'Upcycle')
    )
    food = models.ForeignKey(FoodAdvice, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    eaten = models.CharField(verbose_name = 'Action',max_length=20, null=True, choices=ACTION)
