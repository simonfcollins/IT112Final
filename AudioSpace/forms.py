from django import forms
from .models import Discussion, Forum, Review

class CreateInForum(forms.ModelForm):
    class Meta:
        model= Forum
        fields = '__all__'
 
class CreateInDiscussion(forms.ModelForm):
    class Meta:
        model= Discussion
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
