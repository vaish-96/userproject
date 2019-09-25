# from django import forms
# from django.contrib.admin import widgets 
# from .models import Personal_details,Employee_details

# class Personal_details_form(forms.ModelForm):
    
#     date_of_birth =  forms.DateTimeField(widget = forms.SelectDateWidget())
#     # date_of_birth = forms.DateField(widget=widgets.AdminDateWidget)
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female')
#     )
#     gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    
#     class Meta():
#         model = Personal_details
#         fields ='__all__'

# class Employee_details_form(forms.ModelForm):
    
#     joined_date = forms.DateField(widget = forms.SelectDateWidget())
#     date_of_permanency = forms.DateField(widget = forms.SelectDateWidget())

#     class Meta():
#         model = Employee_details
#         fields ='__all__'
        
