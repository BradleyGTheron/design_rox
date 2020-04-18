from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

# CUSTOMIZATION OF THE USER REGISTRATION FIELDS
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label = '', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label = '', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label = '', max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">Enter the same password as before, for verification.<small></small></span>'

# CUSTOMIZATION OF THE USER REGISTER UPDATE FIELDS
class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''

# CUSTOMIZATION OF THE USER PROFILE FIELDS
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('street_address','suburb','postal_code','city','contact_number')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)



        self.fields['street_address'].widget.attrs['class'] = 'form-control'
        self.fields['street_address'].widget.attrs['placeholder'] = 'Street Address'
        self.fields['street_address'].label = ''
        self.fields['street_address'].help_text = '<span class="form-text text-muted"><small>For shipping purposes.</small></span>'
        self.fields['suburb'].widget.attrs['class'] = 'form-control'
        self.fields['suburb'].widget.attrs['placeholder'] = 'Suburb'
        self.fields['suburb'].label = ''
        self.fields['postal_code'].widget.attrs['class'] = 'form-control'
        self.fields['postal_code'].widget.attrs['placeholder'] = 'Postal Code'
        self.fields['postal_code'].label = ''
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['city'].label = ''
        self.fields['contact_number'].widget.attrs['class'] = 'form-control'
        self.fields['contact_number'].widget.attrs['placeholder'] = 'Contact Number'
        self.fields['contact_number'].label = ''
        self.fields['contact_number'].help_text = '<span class="form-text text-muted"><small>We will never share you contact number</small></span>'

#CUSTOMIZATION OF THE CHANGE PASSWORD FIELDS
class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['old_password'].label = ''
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password1'].label = ''
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].label = ''
