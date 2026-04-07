from django.test import TestCase
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from .models import Trade, HistoricalRate, Profile

class DataIntegrityTests(TestCase):
    """
    Forensic verification of Market Data constraints.
    Proves the 'BlueGamma' cleaning logic works at the database level.
    """
    def setUp(self):
        self.rate_data = {
            "date": "2023-10-05",
            "index_name": "SOFR",
            "tenor": "10Y",
            "rate": 4.50
        }

    def test_historical_rate_creation(self):
        """Test that a valid rate can be created."""
        rate = HistoricalRate.objects.create(**self.rate_data)
        self.assertEqual(str(rate), "2023-10-05 | SOFR | 10Y: 4.5")

    def test_duplicate_prevention(self):
        """
        CRITICAL: Test the unique_together constraint.
        If we try to insert the same Date + Index + Tenor twice, 
        the database MUST reject it.
        """
        HistoricalRate.objects.create(**self.rate_data)
        with self.assertRaises(IntegrityError):
            HistoricalRate.objects.create(**self.rate_data)


class TradeLogicTests(TestCase):
    """
    Verifies the core 'Blotter' functionality and Trade inputs.
    """
    def setUp(self):
        self.user = User.objects.create_user(username='trader1', password='password123')

    def test_trade_creation(self):
        """Test successful creation of a standard Pay-Fixed trade."""
        trade = Trade.objects.create(
            trade_id="TRD-TEST-001",
            user=self.user,
            ticker="USD-SOFR",
            notional=1000000.00,
            tenor_years=5,
            fixed_rate=3.75,
            side="PAY"
        )
        self.assertEqual(trade.strategy, "OUTRIGHT")  # Test default value
        self.assertEqual(str(trade), f"OUTRIGHT | USD-SOFR | {self.user.username}")


class SignalAutomationTests(TestCase):
    """
    Verifies the 'Invisible' logic (Signals).
    This proves that your subscription infrastructure is robust.
    """
    def test_profile_auto_creation(self):
        """
        Test that creating a User AUTOMATICALLY creates a linked Profile.
        This validates the @receiver(post_save) signal in models.py.
        """
        # 1. Create a naked User
        new_user = User.objects.create_user(username='new_subscriber', password='pw')
        
        # 2. Assert the Profile was magically created
        self.assertTrue(hasattr(new_user, 'profile'))
        self.assertFalse(new_user.profile.is_subscriber)  # Should be False by default

    def test_profile_relationship(self):
        """Test the One-to-One relationship integrity."""
        user = User.objects.create_user(username='vip_user', password='pw')
        profile = user.profile
        
        # Verify reverse lookup
        self.assertEqual(profile.user.username, 'vip_user')

