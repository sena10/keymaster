
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField


User = get_user_model()




class UserRegistrationForm(UserCreationForm):
    email = EmailField(label='Email', required=True,
                       help_text="Email pessoal.")

    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = User