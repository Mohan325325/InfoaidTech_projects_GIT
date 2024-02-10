from django.shortcuts import render

# Create your views here.
import random

def roll_dice(request):
    if request.method == 'POST':
        num_dice = int(request.POST.get('num_dice', 2))
        dice_results = [random.randint(1, 6) for _ in range(num_dice)]
        response = render(request, 'Rollerapp/roll_dice.html', {'dice_results': dice_results, 'num_dice': num_dice})
        return response
    return render(request, 'Rollerapp/roll_dice.html')
