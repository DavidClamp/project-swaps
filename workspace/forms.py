from django import forms
from django.core.exceptions import ValidationError
from .models import Trade

class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ['trade_id', 'strategy', 'ticker', 'notional',
                  'tenor_years', 'fixed_rate', 'side', 'group_id']
        
        # WIDGETS: Control HTML rendering
        widgets = {
            'fixed_rate': forms.NumberInput(attrs={
                'step': '0.0001', 
                'placeholder': 'e.g. 0.0450 (for 4.5%)'
            }),
            'notional': forms.NumberInput(attrs={
                'step': '100000', 
                'placeholder': 'e.g. 10000000'
            }),
            'trade_id': forms.TextInput(attrs={
                'placeholder': 'TRD-2026-XXXX'
            }),
            # placeholder example for Group ID
            'group_id': forms.TextInput(attrs={
                'placeholder': 'e.g. STRAT-001 (Leave blank for Outright)',
                'class': 'text-uppercase'  # Optional: Forces visuals to look like codes
            }),

            # STRICT DROPDOWN: Prevents typos (e.g. "Sofr" vs "SOFR")
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
        
        labels = {
            'tenor_years': 'Tenor (Years)',
            'fixed_rate': 'Fixed Rate (Decimal)',
            'ticker': 'Benchmark Index',  # User-friendly label
            'group_id': 'Group ID (Optional for Outright)',
        }

    def clean(self):
        """
            Ensures 'Butterfly' trades are not orphaned without a Group ID.
        """
        cleaned_data = super().clean()
        strategy = cleaned_data.get('strategy')
        group_id = cleaned_data.get('group_id')

        # Logic Rule 1: Butterfly Strategy Integrity
        if strategy == 'FLY' and not group_id:
            self.add_error('group_id', "Butterfly (Fly) strategies require a Group ID to link the legs.")
        
        # Logic Rule 2: Auto-Correction
        if strategy == 'OUTRIGHT' and group_id:
            cleaned_data['group_id'] = None
            
        return cleaned_data
