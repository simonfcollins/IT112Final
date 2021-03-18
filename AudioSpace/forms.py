from django import forms
from .models import Discussion, Forum, Review

class ForumForm(forms.ModelForm):
    class Meta:
        model= Forum
        fields = '__all__'
 
class DiscussionForm(forms.ModelForm):
    class Meta:
        model= Discussion
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
