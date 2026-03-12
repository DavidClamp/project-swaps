from django import forms
from .models import Trade

class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ['trade_id', 'strategy', 'ticker', 'notional', 
                  'tenor_years', 'fixed_rate', 'side', 'group_id']
        widgets = {
            'fixed_rate': forms.NumberInput(attrs={'step': '0.0001', 'placeholder': '0.0450'}),
            'notional': forms.NumberInput(attrs={'placeholder': '10000000'}),
        }
