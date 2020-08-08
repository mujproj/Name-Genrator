from django import forms

class main(forms.Form):
    def __init__(self, *args, **kwargs):
        super(main, self).__init__(*args, **kwargs)
        self.fields['string1'].label = "Name 1"
        self.fields['string2'].label = "Name 2"
        self.fields['gender'].label = "Select Gender"
        self.fields['origin'].label = "Select A origin Or Type of Name"

    CHOICE1 = (
        ("Select", "Select"),
        ("Female", "Female"),
        ("Male", "Male"),
    )

    CHOICE2 = (
        ("Select", "Select"),
        ("Indian", "Indian"),
        ("American", "American"),
        ("British", "British"),
        ("French", "French"),
        ("German", "German"),
        ("Italian", "Italian")
    )
    string1 = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}))
    string2 = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}))
    gender = forms.ChoiceField(choices=CHOICE1)
    origin = forms.ChoiceField(choices=CHOICE2)