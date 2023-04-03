from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    desc = forms.CharField(max_length=500, label="Description", required=False)
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=300)
    password = forms.CharField(max_length=300, widget=forms.PasswordInput)