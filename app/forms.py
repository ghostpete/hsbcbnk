from django import forms
from .models import Transfer
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = [
            'from_account', 'account_holder_name', 'account_number', 
            'ach_routing', 'account_type', 'bank_name', 'amount', 'address'
        ]
        
        widgets = {
            'from_account': forms.Select(attrs={
                'class': 'form-control', 
                'placeholder': 'Select Account',
            }),
            'account_holder_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Account Holder Name',
            }),
            'account_number': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Account Number',
            }),
            'ach_routing': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'ACH Routing Number',
            }),
            'account_type': forms.Select(attrs={
                'class': 'form-control', 
                'placeholder': 'Account Type',
            }),
            'bank_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Bank Name',
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Transfer Amount',
                'min': '0.01',  # Minimum value to avoid negative amounts
                'step': '0.01',  # For decimal input
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Bank Address',
            }),
        }



# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'annual_income', 'employment_status', 'preferred_account_type', 'ssn', 'profile_image']
        
#         widgets = {
#             'first_name': forms.TextInput(attrs={
#                 'class': 'form-control form-control-lg',
#                 'placeholder': 'Enter your first name'
#             }),
#             'last_name': forms.TextInput(attrs={
#                 'class': 'form-control form-control-lg',
#                 'placeholder': 'Enter your last name'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'form-control form-control-lg',
#                 'placeholder': 'Enter your email'
#             }),
#             'phone_number': forms.TextInput(attrs={
#                 'class': 'form-control form-control-lg',
#                 'placeholder': 'Enter your phone number'
#             }),
#             'address': forms.Textarea(attrs={
#                 'class': 'form-control form-control-lg',
#                 'placeholder': 'Enter your address',
#                 'rows': 3
#             }),
#             'annual_income': forms.TextInput(attrs={
#                 'class': 'form-control form-control-lg',
#                 'placeholder': 'Enter your annual income'
#             }),
#             'employment_status': forms.Select(attrs={
#                 'class': 'form-control form-control-lg',
#             }),
#             'preferred_account_type': forms.Select(attrs={
#                 'class': 'form-control form-control-lg',
#             }),
#             'ssn': forms.TextInput(attrs={
#                 'class': 'form-control form-control-lg',
#                 'placeholder': 'Enter your SSN'
#             }),
#             'profile_image': forms.FileInput(attrs={
#                 'class': 'form-control form-control-lg',
#             })
#         }

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if CustomUser.objects.filter(email=email).exists():
#             raise forms.ValidationError("Email already exists.")
#         return email

#     def clean_phone_number(self):
#         phone_number = self.cleaned_data.get('phone_number')
#         if CustomUser.objects.filter(phone_number=phone_number).exists():
#             raise forms.ValidationError("Phone number already exists.")
#         return phone_number
    


        