from django.contrib.auth.forms import UserCreationForm , UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from post.models import Profile


        
class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'linkedin_url', 'github_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the title'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'linkedin_url': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the content'}),
            'github_url': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the content'}),        
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
                        
                        
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    date_joined = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'date_joined')
     

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    
    class Meta:
        model = User
        fields = ('old_password, ''new_password1', 'new_password2')
    