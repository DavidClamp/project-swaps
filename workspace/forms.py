from django import forms
from django.core.exceptions import ValidationError
from .models import Trade

class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ['trade_id', 'strategy', 'ticker', 'notional', 'forward_start',
                  'tenor_years', 'fixed_rate', 'side', 'group_id']
        
        # WIDGETS: Control HTML rendering and Default Values
        widgets = {
            'fixed_rate': forms.NumberInput(attrs={
                'step': '0.0001', 
                'placeholder': 'e.g. 0.0450 (for 4.5%)'
            }),
            'notional': forms.NumberInput(attrs={
                'step': '100000', 
                'placeholder': 'e.g. 10000000'
            }),
            
            # FORWARD START: 
            'forward_start': forms.NumberInput(attrs={
                'step': '0.25', 
                'placeholder': '0.0 (Spot)',
                'value': '0.0'  
            }),

            'trade_id': forms.TextInput(attrs={
                'placeholder': 'TRD-2026-XXXX'
            }),
            
            'group_id': forms.TextInput(attrs={
                'placeholder': 'e.g. STRAT-001 (Leave blank for Outright)',
                'class': 'text-uppercase'
            }),

            # DROPDOWNS: 
            'ticker': forms.Select(choices=[
                ('USD-SOFR', 'USD - SOFR (Secured Overnight)'),
                ('EUR-EURIBOR', 'EUR - EURIBOR'),
                ('GBP-SONIA', 'GBP - SONIA'),
            ]),
            
            'strategy': forms.Select(choices=[
                ('OUTRIGHT', 'Outright (Single Leg)'),
                ('CURVE', 'Curve (Steepener/Flattener)'),
                ('FLY', 'Butterfly (Fly)'),
            ]),
        }
        
        # LABELS:
        labels = {
            'forward_start': 'Start Delay (Years)', 
            'tenor_years': 'Tenor (Years)',
            'fixed_rate': 'Fixed Rate (Decimal)',
            'ticker': 'Benchmark Index',
            'group_id': 'Group ID (Optional for Outright)',
        }

    def clean(self):
        """
        CROSS-FIELD VALIDATION: 
        Ensures complex strategies (like Butterfly) are not orphaned.
        """
        cleaned_data = super().clean()
        strategy = cleaned_data.get('strategy')
        group_id = cleaned_data.get('group_id')

        # Logic Rule 1: Butterfly Strategy Integrity
        if strategy == 'FLY' and not group_id:
            self.add_error('group_id', "Butterfly (Fly) strategies require a Group ID to link the legs.")
        
        # Logic Rule 2: Auto-Correction (Cleanup)
        if strategy == 'OUTRIGHT' and group_id:
            cleaned_data['group_id'] = None
            
        return cleaned_data
    
    def clean_forward_start(self):
        """
        UX SAFETY NET: 
        If the user clears the input (None/Empty), silently default 
        to 0.0 (Spot) instead of raising a 'This field is required' error.
        """
        data = self.cleaned_data.get('forward_start')
        
        # 1. Handle Empty Input -> Default to Spot
        if data is None:
            return 0.0
            
        # 2. Handle Logic Error -> Prevent Past Dates
        if data < 0:
            raise forms.ValidationError("Start delay cannot be in the past.")
            
        return data
