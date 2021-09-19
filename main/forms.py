from django import forms
from .models import Review, Dish


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('stars', 'review_text')

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['stars'].widget.attrs = {'min': 1, 'max': 5}

    def clean(self):
        super(ReviewForm, self).clean()
        stars = self.cleaned_data.get('stars')
        if isinstance(stars, type(None)):
            self._errors['stars'] = self.error_class(['You must give a dish a star rating'])
        else:
            if stars < 1:
                self._errors['stars'] = self.error_class(['You must give at minimum 1 star'])
            elif stars > 5:
                self._errors['stars'] = self.error_class(['You must give at maximum 5 stars'])
        return self.cleaned_data


class DishImageForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('image',)
