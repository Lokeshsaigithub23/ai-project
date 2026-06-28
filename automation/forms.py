from django import forms
class UserInputForm(forms.Form):
    topic = forms.CharField(
        required=False,
        label="Topic",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Topic..."
            }
        )
    )
    image = forms.ImageField(
        required=False,
        label="Upload Image"
    )