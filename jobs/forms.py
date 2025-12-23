from django import forms

class JobSearchForm(forms.Form):
    designation = forms.CharField(
        label="Designation",
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Python Developer",
            "class": "w-full rounded-md border-gray-300 shadow-sm p-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"
        })
    )

    location = forms.CharField(
        label="City / Location",
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Ahmedabad",
            "class": "w-full rounded-md border-gray-300 shadow-sm p-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"
        })
    )

    EXPERIENCE_CHOICES = [
        (0, "Fresher"),
        (1, "1-3 Years"),
        (2, "3-5 Years"),
    ]


    experience = forms.ChoiceField(
        label="Experience Level",
        choices=EXPERIENCE_CHOICES,
        widget=forms.Select(attrs={
            "class": "w-full rounded-md border-gray-300 shadow-sm p-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"
        })
    )
