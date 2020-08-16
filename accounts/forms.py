from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
      class Meta:
            model = User
            fields = [
                'username',
                'email',
                'password1',
                'password2',
            ]

