from django.shortcuts import render
import requests
from .forms import DietaryForm

base_url = "http://localhost:8080"


def get_diet_plan(request):
    if request.method == 'GET':
        form = DietaryForm(request.GET)
        if form.is_valid():
            params = form.cleaned_data
            res = requests.get(f'{base_url}/optimal-diet?', params=params)
            # the returned JSON is automatically deserialized
            diet_plan = res.json() if res.status_code == 200 else None
            return render(request, 'diet_plan.html', {'diet_plan': diet_plan})
    else:
        form = DietaryForm()
    return render(request, 'diet_plan.html', {'form': form})
