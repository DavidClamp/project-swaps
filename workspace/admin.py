from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import HistoricalRate, Trade, Profile

@admin.register(HistoricalRate)
class HistoricalRateAdmin(admin.ModelAdmin):
    list_display = ('date', 'index_name', 'tenor', 'rate')
    list_filter = ('index_name', 'tenor')

@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('trade_id', 'user', 'strategy', 'ticker', 'last_npv')
    search_fields = ('trade_id', 'ticker')

 # Toggle PRO status
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_subscriber', 'stripe_customer_id')
    list_editable = ('is_subscriber',) 
    