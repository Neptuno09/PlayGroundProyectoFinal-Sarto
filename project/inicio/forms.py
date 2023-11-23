from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import UserProfile, BlogEntry
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password1', 'password2')  # Excluyendo 'email'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password')  # Asegúrate de incluir los campos necesarios

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )
class AvatarForm(forms.ModelForm):
    avatar = forms.ImageField()
    
    class Meta:
        model = UserProfile
        fields = ["avatar"]
class BioForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = UserProfile
        fields = ["bio"]

class UserProfileSearchForm(forms.Form):
    query = forms.CharField(label='Buscar por nombre de usuario',max_length=100,required=False,
    widget=forms.TextInput(attrs={'placeholder': 'Escribe aquí'})
    )
class BlogEntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = ['Titulo','Subtitulo','Texto','Imagen']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Imagen'].required = False
    
from django import forms

class MessageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)




