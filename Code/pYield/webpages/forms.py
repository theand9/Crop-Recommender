from django import forms
from . import models

district_choice = [
    (u'', u'---Select Your District---'),
    ('Akola', 'Akola'),
    ('Amravati', 'Amravati'),
    ('Aurangabad', 'Aurangabad'),
    ('Beed', 'Beed'),
    ('Bhandara', 'Bhandara'),
    ('Bhuldhana', 'Bhuldhana'),
    ('Chandrapur', 'Chandrapur'),
    ('Dhule', 'Dhule'),
    ('Gadchiroli', 'Gadchiroli'),
    ('Gondia', 'Gondia'),
    ('Hingoli', 'Hingoli'),
    ('Jalgaon', 'Jalgaon'),
    ('Jalna', 'Jalna'),
    ('Kolhapur', 'Kolhapur'),
    ('Latur', 'Latur'),
    ('Nagpur', 'Nagpur'),
    ('Nanded', 'Nanded'),
    ('Nandurbar', 'Nandurbar'),
    ('Nashik', 'Nashik'),
    ('Osmanabad', 'Osmanabad'),
    ('Parbhani', 'Parbhani'),
    ('Pune', 'Pune'),
    ('Raigad', 'Raigad'),
    ('Ratnagiri', 'Ratnagiri'),
    ('Sangli', 'Sangli'),
    ('Satara', 'Satara'),
    ('Sindhudurg', 'Sindhudurg'),
    ('Solhapur', 'Solhapur'),
    ('Thane', 'Thane'),
    ('Wardha', 'Wardha'),
    ('Washim', 'Washim'),
    ('Yavatmal', 'Yavatmal'),
]

# village_list = models.Akola.objects.values('village_Name',flat=True)


class FarmerRegistrationForm(forms.Form):

    farmer_Name = forms.CharField(max_length=30,
                                  widget=forms.TextInput(attrs={
                                      'placeholder': 'Enter Your Full Name',
                                      'class': 'form-control',
                                      'id': 'name',
                                  }))

    phone_Number = forms.CharField(max_length=10,
                                   widget=forms.NumberInput(attrs={
                                       'placeholder': 'Enter your Phone Number',
                                       'class': 'form-control',
                                       'id': 'phone',
                                       'oninput': 'limit_phoneNumber()',
                                       'unique': True,
                                   }))

    areaInHectare = forms.FloatField(required=False, max_value=20,                                              min_value=0,
                                     widget=forms.NumberInput(attrs={
                                         'class': 'form-control',
                                         'placeholder': 'Enter your Area in Hectare',
                                         'id': 'area',
                                     }))

    aadhar_Number = forms.CharField(max_length=12,
                                    widget=forms.NumberInput(attrs={
                                        'placeholder': 'Enter your Aadhar card Number',
                                        'class': 'form-control',
                                        'id': 'aadhar',
                                        'oninput': 'limit_aadharNumber()',
                                        # 'onkeyup': 'addHyphen(this)',
                                        'primary_key': True,
                                    }))

    district = forms.CharField(max_length=20,
                               widget=forms.Select(choices=district_choice, attrs={
                                   'class': 'form-control',
                                   'id': 'district',
                               }))

    village = forms.CharField(max_length=30,
                              widget=forms.TextInput(attrs={
                                  'placeholder': 'Enter Your Village Name',
                                  'class': 'form-control',
                                  'id': 'village',
                              }))


class FarmerDetailsForm(forms.Form):
    farmer_Name = forms.CharField(max_length=30,
                                  widget=forms.TextInput(attrs={
                                      'placeholder': 'Enter Your Full Name',
                                      'class': 'form-control',
                                  }))

    aadhar_Number = forms.CharField(max_length=12,
                                    widget=forms.NumberInput(attrs={
                                        'placeholder': 'Enter Aadhar card Number',
                                        'class': 'form-control',
                                        'id': 'aadhar',
                                        'oninput': 'limit_aadharNumber()',
                                        # 'onkeyup': 'addHyphen()',
                                        'style': 'padding:20px;',
                                    }))
