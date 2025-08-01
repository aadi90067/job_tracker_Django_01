from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount']
        widgets = {
            'category': forms.Select(choices=[
                ('Food', 'Food'),
                ('Shopping', 'Shopping'),
                ('EMI/Loans', 'EMI/Loans'),
                ('Entertainment', 'Entertainment'),
                ('Transport', 'Transport'),
                ('Medical', 'Medical'),
                ('Utilities', 'Utilities'),
                ('Personal Care', 'Personal Care'),
                ('Savings', 'Savings'),
                ('Donations', 'Donations'),
                ('Education', 'Education'),
                ('Household Items', 'Household Items'),
                ('Pets', 'Pets'),
            ]),
            'amount': forms.NumberInput(attrs={
                'placeholder': 'Enter amount',
                'min': '1',
                'step': '0.01'
            })
        }
