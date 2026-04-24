from django import forms
from django.core.exceptions import ValidationError
from .models import Trade


class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = [
            "trade_id",
            "strategy",
            "ticker",
            "notional",
            "forward_start",
            "tenor_years",
            "fixed_rate",
            "side",
            "group_id",
        ]

        # WIDGETS: Control HTML rendering
        widgets = {
            "fixed_rate": forms.NumberInput(
                attrs={"step": "0.01", "placeholder": "4.00 (Enter as %)"}
            ),
            "notional": forms.NumberInput(
                attrs={"step": "100000", "placeholder": "10,000,000"}
            ),
            "forward_start": forms.NumberInput(
                attrs={"step": "0.25", "placeholder": "0.0 (Spot)"}
            ),
            "trade_id": forms.TextInput(
                attrs={"placeholder": "TRD-2026-XXXX"}
            ),
            "group_id": forms.TextInput(
                attrs={
                    "placeholder": "e.g. STRAT-001",
                    "class": "text-uppercase",
                }
            ),
        }

        # LABELS: Clear instruction to user
        labels = {
            "forward_start": "Start Delay (Years)",
            "tenor_years": "Tenor (Years)",
            "fixed_rate": "Fixed Rate (%)",
            "ticker": "Benchmark Index",
            "group_id": "Group ID ( Can leave blank for Outright)",
        }

    def clean(self):
        """
        CROSS-FIELD VALIDATION:
        Ensures complex strategies (like Butterfly) are not orphaned.
        """
        cleaned_data = super().clean()
        strategy = cleaned_data.get("strategy")
        group_id = cleaned_data.get("group_id")

        # Logic Rule 1: Butterfly Strategy Integrity
        if strategy == "FLY" and not group_id:
            self.add_error(
                "group_id",
                "Butterfly (Fly) strategies require a Group ID to link the legs.",
            )

        # Logic Rule 2: Auto-Correction (Cleanup)
        # if strategy == "OUTRIGHT" and group_id:
        #     cleaned_data["group_id"] = None

        # return cleaned_data

    def clean_forward_start(self):
        """
        UX SAFETY NET:
        Handle empty input gracefully.
        """
        data = self.cleaned_data.get("forward_start")
        if data is None:
            return 0.0
        if data < 0:
            raise forms.ValidationError("Start delay cannot be in the past.")
        return data
