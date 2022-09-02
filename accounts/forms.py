from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Profile
from django.forms import ModelForm

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'first_name', 'last_name', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields['username'].label = ""
            self.fields['first_name'].label = ""
            self.fields['last_name'].label = ""
            self.fields['email'].label = ""
            self.fields['password1'].label = ""
            self.fields['password2'].label = ""
    class Meta:
        model = User        
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']