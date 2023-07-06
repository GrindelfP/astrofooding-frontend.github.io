from django.shortcuts import render
import requests
from .forms import DietaryForm
from math import ceil

base_url_local = "http://localhost:8080"
base_url_remote = "http://astrofooding-ducayxikeq-lz.a.run.app"


def get_diet_plan(request):
    if request.method == 'GET':
        form = DietaryForm(request.GET)
        if form.is_valid():
            params = form.cleaned_data
            res = requests.get(f'{base_url_remote}/optimal-diet?', params=params, verify=False)
            # the returned JSON is automatically deserialized
            diet_plan = res.json() if res.status_code == 200 else None

            if diet_plan:
                total_protein = 0
                total_fat = 0
                total_carbs = 0
                total_weight = 0

                for meal in diet_plan['mealsByQuantity']:
                    total_protein += meal['meal']['protein'] * meal['quantity']
                    total_fat += meal['meal']['fat'] * meal['quantity']
                    total_carbs += meal['meal']['carbs'] * meal['quantity']
                    total_weight += meal['meal']['weight'] * meal['quantity']

                total_protein = ceil(total_protein)
                total_fat = ceil(total_fat)
                total_carbs = ceil(total_carbs)
                total_weight = ceil(total_weight)

                # Round macronutrient values to the nearest integer
                diet_plan['macronutrients']['calories'] = ceil(diet_plan['macronutrients']['calories'])
                diet_plan['macronutrients']['protein'] = ceil(diet_plan['macronutrients']['protein'])
                diet_plan['macronutrients']['fat'] = ceil(diet_plan['macronutrients']['fat'])
                diet_plan['macronutrients']['carbs'] = ceil(diet_plan['macronutrients']['carbs'])

                return render(request, 'diet_plan.html', {'diet_plan': diet_plan, 'total_protein': total_protein, 'total_fat': total_fat, 'total_carbs': total_carbs, 'total_weight': total_weight})

    else:
        form = DietaryForm()
    return render(request, 'diet_plan.html', {'form': form})
