from django import forms
from .models import Game, Review

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["title", "platform", "hours_played"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "e.g., Elden Ring"}),
            "platform": forms.TextInput(attrs={"placeholder": "PC, PS5, Switch..."}),
            "hours_played": forms.NumberInput(attrs={"step": "0.1", "min": "0"}),
        }


class ReviewForm(forms.ModelForm):
    # Explicit field definition to enforce 1–10 range (defined type + validation)
    rating = forms.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Review
        fields = ["game", "rating", "headline", "body", "finished"]
        widgets = {
            "headline": forms.TextInput(attrs={"placeholder": "Short summary headline"}),
            "body": forms.Textarea(attrs={"rows": 6, "placeholder": "Write your full review..."}),
        }
