from .models import current_meal_models


def current_meal(request):
    return {'current_meal': current_meal_models()}
