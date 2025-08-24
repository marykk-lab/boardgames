from django import forms
from .models import Order, Game
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta():
        model = User
        fields = ("username", "email", "password1", "password2")


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "user",
            #"games", #is this correct?
            "count",
            "total_price",
            "country",
            "city",
            "address",
        ]
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            "title",
            "description",
            "price",
            "image",
            "rating",
            "count",
        ]

class UserGroupForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    def save(self):
        user = self.cleaned_data['user']
        group = self.cleaned_data['group']
        user.groups.add(group)
        user.save()

class GameDeleteForm(forms.Form):
    game = forms.ModelChoiceField(queryset=Game.objects.all())
    def delete(self):
        game = self.cleaned_data['game']
        game.delete()