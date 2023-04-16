from django.forms import ModelForm
from .models import Feeding

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        field = ['date', 'meal']