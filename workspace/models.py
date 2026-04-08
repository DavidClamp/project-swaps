from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class HistoricalRate(models.Model):
    """Global Market Data Store: SOFR, SONIA, TONA, EURIBOR, etc."""

    INDEX_CHOICES = [
        ('SOFR', 'USD SOFR'),
        ('SONIA', 'GBP SONIA'),
        ('EURIBOR', 'EUR EURIBOR'),
        ('ESTR', 'EUR €STR'),
        ('TONA', 'JPY TONA'),
        ('TIBOR', 'JPY TIBOR'),
        ('SARON', 'CHF SARON'),
        ('JIBAR', 'ZAR JIBAR'),
        ('WIBOR', 'PLN WIBOR'),
    ]

    date = models.DateField(db_index=True)
    index_name = models.CharField(max_length=10, choices=INDEX_CHOICES)
    tenor = models.CharField(max_length=10)
    rate = models.FloatField()

    class Meta:
        unique_together = ('date', 'index_name', 'tenor')
        ordering = ['-date', 'index_name']

    def __str__(self):
        return f"{self.date} | {self.index_name} | {self.tenor}: {self.rate}"


class Trade(models.Model):
    """IRS Trade Blotter: Supports Outrights and Butterflies """
    STRATEGY_CHOICES = [('OUTRIGHT', 'Outright'), ('FLY', 'Butterfly')]
    SIDE_CHOICES = [('PAY', 'Pay Fixed'), ('REC', 'Rec Fixed')]

    trade_id = models.CharField(max_length=20, unique=True, help_text="Custom Trade ID (e.g. TRD-001)")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trades")
    strategy = models.CharField(max_length=10, choices=STRATEGY_CHOICES, default='OUTRIGHT')
    group_id = models.CharField(max_length=50, blank=True, null=True, help_text="Links Butterfly legs")

    ticker = models.CharField(max_length=20)
    notional = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    forward_start = models.FloatField(
        default=0.0,
        blank=True,  # Allows form to be submitted even if empty
        verbose_name="Start Delay (Years)"
    )
    tenor_years = models.PositiveIntegerField()
    fixed_rate = models.FloatField()
    side = models.CharField(max_length=3, choices=SIDE_CHOICES)
    weight = models.FloatField(default=1.0)

    # QuantLib/Pandas Outputs
    last_npv = models.FloatField(null=True, blank=True)
    pv01 = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.strategy} | {self.ticker} | {self.user.username}"


class Profile(models.Model):
    """
    Extends User to track subscription status.
    Required for the 'can_access_butterfly_analytics' gating in utils.py.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_subscriber = models.BooleanField(default=False)
    stripe_customer_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Automatically creates a Profile whenever a new User is registered."""
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
