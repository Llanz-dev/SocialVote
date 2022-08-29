from django.forms import ModelForm
from .models import Poll

class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['img', 'question', 'question_one', 'question_two', 'question_three']
