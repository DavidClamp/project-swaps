import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def subscription_plans(request):
    return render(request, "workspace/plans.html")


@login_required
def create_checkout_session(request):
    #  If no email, use a placeholder or show error
    if request.user.email:
        user_email = request.user.email
    else:
        user_email = f"{request.user.username}@example.com"
    try:
        checkout_session = stripe.checkout.Session.create(
            customer_email=user_email,
            payment_method_types=["card"],
            line_items=[{"price": settings.STRIPE_PRICE_ID, "quantity": 1}],
            mode="subscription",
            success_url=request.build_absolute_uri("/payment-success/"),
            cancel_url=request.build_absolute_uri("/payment-cancelled/"),
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        messages.error(request, f"Stripe Error: {str(e)}")
        return redirect("subscription")


@login_required
def payment_success(request):
    profile = request.user.profile
    profile.is_subscriber = True
    profile.save()
    return render(request, "workspace/payment_success.html")
