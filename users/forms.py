from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Extend UserCreation Form
class CustomUserCreationForm(UserCreationForm):
    class Meta: 
        model = get_user_model() 
        fields = ('email', 'username',)
# User Update Form
class CustomUserUpdateForm(UserCreationForm):
    class Meta: 
        model = get_user_model() 
        fields = ('email',)
        exclude = ["password"]

# Extend UserChange Form
class CustomUserChangeForm(UserChangeForm):
    class Meta:  
        model = get_user_model()
        fields = ('email', 'username',)
