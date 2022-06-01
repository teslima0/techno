from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

# Create a UserUpdateForm to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [ 'first_name','last_name','username', 'email']

# Create a ProfileUpdateForm to update image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

'''
class ProfilePageForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('bio','profile_pic')
        widgets={

                'bio': forms.Textarea(attrs={'class':'form-control'}),
              # 'profile_pic': forms.TextInput(attrs={'class':'form-control'}),
               #'author': forms.Select(attrs={'class':'form-control'}),            
                
    }

class SignUpForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model= User
        fields=('username','first_name','last_name','email','password1','password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'
'''