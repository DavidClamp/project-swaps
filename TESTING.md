# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.


## 1. Testing Strategy & Methodology

The testing strategy for IRSQuant follows a hybrid approach, combining automated unit tests for financial logic with extensive manual testing for UI/UX, responsiveness, and defensive programming.

### Testing Phases

1. **Validator Auditing:**  W3C HTML, Jigsaw CSS, CI Python Linter

2.  **Responsive Stress Testing:** Hybrid Navbar + 4 breakpoints (PEP8)

3. **Logical Data Testing:** BlueGamma‑inspired data cleaning and validation, and numerical integrity checks

4. **Lighthouse Auditing:** Performance, Accessibility, SEO

5. **Defensive Programming:** Form validation, access control, error handling and user‑flow protection
 
6. **User Story Testing:** Verifying each user story is fully satisfied by implemented features

7. **Automated Testing:** Django unittest suite + Coverage reporting

---

## 1. Code Validation

### HTML Validation

I have used the [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

Because Django templates contain {% tags %} and {{ variables }}, validation was performed using:

1. Open rendered page

2. View Page Source

3. Copy compiled HTML

4. Validate via “Validate by Input”



| Directory | File | Status | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| templates | [base.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/base.html) | ⚠️Minor   | ![screenshot](documentation/validation/w3cvalidation_base.png) | Minor warnings (template tags ignored by validator) |
| templates | [footer.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/footer.html) | ⚠️Minor | ![screenshot](documentation/validation/w3cvalidation_footer.png) | Minor warnings| 
|templates | [navbar.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/navbar.html) | ⚠️Minor | ![screenshot](documentation/validation/w3cvalidation_edittrade.png) | Minor warnings |
 templates | [navbar.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/navbar.html) | ⚠️Minor | ![screenshot](documentation/validation/w3cvalidation_navbar.png) | Minor Warnings |
| workspace | [404.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/404.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_404.png) | Minor related warnings |
| workspace | [500.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/500.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_500.png) | Minor warnings |
| workspace | [add_trade.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/add_trade.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_addtrade.png) | Minor warnings |
| workspace | [analyser.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/analyser.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_analyser.png) | Minor warnings |
| workspace | [blotter.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/blotter.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_blotter.png) | Minor warnings |
| workspace | [curve_bars.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/curve_bars.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_curvebars.png) | Minor warnings |
| workspace | [dashboard.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/dashboard.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_dashboard.png) | Minor warnings |
| workspace | [delete_confirm.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/delete_confirm.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_deleteconfirm.png) | Minor warnings |
| workspace | [edit_trade.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/edit_trade.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_edittrade.png) | Minor warnings |
| workspace | [histogram.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/histogram.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_histogram.png) | Minor warnings |
| workspace | [payment_cancelled.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/payment_cancelled.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_paymentcancelled.png) | Minor warnings |
| workspace | [payment_success.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/payment_success.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_paymentsuccess.png) | Minor warnings |
| workspace | [plans.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/plans.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_plans.png) | Minor warnings |
| account | [login.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/account/login.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_login.png) | Minor warnings |
| account | [logout.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/account/logout.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_logout.png) | Minor warnings |
| account | [password_reset.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/account/password_reset.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_passwordreset.png) | Minor warnings |
| account | [signup.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/account/signup.html) | ⚠️ Minor | ![screenshot](documentation/validation/w3cvalidation_signup.png) | Minor warnings |

---

All warnings were related to Django template syntax and not actual HTML errors.


### CSS Validation
I have used the [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/) to validate my custom CSS.

| Directory | File | Status | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [style.css](https://github.com/DavidClamp/project-swaps/blob/main/static/css/style.css) | ✅ PASS | ![screenshot](documentation/validation/w3ccssvalidation.png) | All root variables and vendor prefixes validated successfully vendor prefixes. |
---


### Python Validation
All Python code was checked using the **CI Python Linter** (PEP8 standard).

**NOTE**: `E501 line too long` 

Where possible, long lines were refactored. Some Django‑generated or settings‑related lines cannot be shortened without breaking functionality.


| Directory | File | URL | Status | Screenshot | Notes |
| --- | --- | --- | --- | --- | --- |
| 
| Root | [manage.py](https://github.com/DavidClamp/project-swaps/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/manage.py) | ✅ PASS |![screenshot](documentation/linter/linter_manage.png) | All clear, no errors found|
| swapanalyser | [signals.py](https://github.com/DavidClamp/project-swaps/blob/main/swapanalyser/signals.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/swapanalyser/signals.py) | ✅ PASS |![screenshot](documentation/linter/linter_signals.png) | All clear, no errors found |
| swapanalyser | [settings.py](https://github.com/DavidClamp/project-swaps/blob/main/swapanalyser/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/swapanalyser/settings.py) | ✅ PASS |![screenshot](documentation/linter/linter_settings.png) | E501 lines too long > 79 characters |
| swapanalyser | [urls.py](https://github.com/DavidClamp/project-swaps/blob/main/swapanalyser/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/swapanalyser/urls.py) | ✅ PASS |![screenshot](documentation/linter//linter_url.png) | All clear, no errors found |
| workspace | [admin.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/admin.py) |  ✅ PASS |![screenshot](documentation/linter/linter_admin.png) | All clear, no errors found |
| workspace | [checkout_views.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/checkout_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/checkout_views.py) |  ✅ PASS |![screenshot](documentation/linter/linter_checkout.png) | All clear, no errors found | 
| workspace | [choices.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/choices.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/choices.py) |  ✅ PASS |![screenshot](documentation/linter/linter_choices.png) | All clear, no errors found |
| workspace | [data_handler.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/data_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/data_handler.py) |  ✅ PASS |![screenshot](documentation/linter/linter_datahandler.png) | E501 line too long > 79 characters |
| workspace | [forms.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/forms.py) |  ✅ PASS |![screenshot](documentation/linter/linter_forms.png) | E501 lines too long > 79 characters |
| workspace | [models.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/models.py) |  ✅ PASS |![screenshot](documentation/linter/linter_models.png) | All clear, no errors found |![screenshot](documentation/validation/py-workspace-models.png) | ⚠️ | Minor warnings |
| workspace | [tests.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/tests.py) | ✅ PASS |![screenshot](documentation/linter/linter_tests.png) |E501 lines too long > 79 characters |
| workspace | [utils.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/utils.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/utils.py) |  ✅ PASS |![screenshot](documentation/linter/linter_utils.png) | All clear, no errors found |
| workspace | [views.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/views.py) | ✅ PASS |![screenshot](documentation/linter/linter_views.png) | All clear, no errors found |

---

## 2. Responsive Testing

### Responsiveness

Responsiveness was tested across mobile, tablet and desktop breakpoints.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Sign in | ![screenshot](documentation/responsiveness/mobile_signin.png) | ![screenshot](documentation/responsiveness/laptop_signin.png) | ![screenshot](documentation/responsiveness/desktop_signin.png) | Works as expected |
| Sign out | ![screenshot](documentation/responsiveness/mobile_signout.png) | ![screenshot](documentation/responsiveness/laptop_signout.png) | ![screenshot](documentation/responsiveness/desktop_signout.png) | Works as expected |
| Subscription | ![screenshot](documentation/responsiveness/mobile_subscription.png) | ![screenshot](documentation/responsiveness/laptop_subscription.png) | ![screenshot](documentation/responsiveness/desktop_subscription.png) | Works as expected |
| Dashboard| ![screenshot](documentation/responsiveness/mobile_dashboard.png) | ![screenshot](documentation/responsiveness/laptop_dashboard.png) | ![screenshot](documentation/responsiveness/desktop_dashboard.png) | Works as expected |
| Blotter | ![screenshot](documentation/responsiveness/mobile_blotter.png) | ![screenshot](documentation/responsiveness/laptop_blotter.png) | ![screenshot](documentation/responsiveness/desktop_blotter.png) | Works as expected |
| Analyser | ![screenshot](documentation/responsiveness/mobile_analyser.png) | ![screenshot](documentation/responsiveness//laptop_analyser.png) | ![screenshot](documentation/responsiveness/desktop_analyser.png) | Works as expected |
| Term Structure | ![screenshot](documentation/responsiveness/laptop_term.png) | ![screenshot](documentation/responsiveness/laptop_term.png) | ![screenshot](documentation/responsiveness/desktop_term.png) | Work as expected |
| Rate History | ![screenshot](documentation/responsiveness/mobile_history.png) | ![screenshot](documentation/responsiveness/laptop_history.png) | ![screenshot](documentation/responsiveness/desktop_history.png) | Work as expected |
| Add Trade| ![screenshot](documentation/responsiveness/mobile_addtrade.png) | ![screenshot](documentation/responsiveness/laptop_addtrade.png) | ![screenshot](documentation/responsiveness/desktop_addtrade.png) | Works as expected |
| Edit Trade| ![screenshot](documentation/responsiveness/mobile_edittrade.png) | ![screenshot](documentation/responsiveness/laptop_edittrade.png) | ![screenshot](documentation/responsiveness/desktop_edittrade.png) | Works as expected |
| Delete Trade| ![screenshot](documentation/responsiveness/mobile_confirmdelete.png) | ![screenshot](documentation/responsiveness/laptop_confirmdelete.png) | ![screenshot](documentation/responsiveness/mobile_confirmdelete.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile_404.png) | ![screenshot](documentation/responsiveness/laptop_404.png) | ![screenshot](documentation/responsiveness/desktop_404.png) | Works as expected |
| 500 | ![screenshot](documentation/responsiveness/mobile_500.png) | ![screenshot](documentation/responsiveness/laptop_500.png) | ![screenshot](documentation/responsiveness/desktop_500.png) | Works as expected |

---

## 3. Browser Compatibility

The deployed project was tested across the three major browsers to ensure consistent rendering, layout stability, and functional parity.

| Page | Chrome | Firefox | Edge | Notes |
| --- | --- | --- | --- | --- |
| Sign in | ![screenshot](documentation/responsiveness/desktop_signin.png) | ![screenshot](documentation/browser/firefox_signin.png) | ![screenshot](documentation/browser/edge_signin.png) | Works as expected |
| sign out | ![screenshot](documentation/responsiveness/desktop_signout.png) | ![screenshot](documentation/browser/firefox_signout.png) | ![screenshot](documentation/browser/edge_signout.png) | Works as expected |
| Dashboard | ![screenshot](documentation/responsiveness/desktop_dashboard.png) | ![screenshot](documentation/browser/firefox_dashboard.png) | ![screenshot](documentation/browser/edge_dashboard.png) | Works as expected |
| Blotter | ![screenshot](documentation/responsiveness/desktop_blotter.png) | ![screenshot](documentation/browser/firefox_blotter.png) | ![screenshot](documentation/browser/edge_blotter.png) | Works as expected |
| Analyser | ![screenshot](documentation/responsiveness/desktop_analyser.png) | ![screenshot](documentation/browser/firefox_analysis.png) | ![screenshot](documentation/browser/edge_analyser.png) | Works as expected |
| Term Structure | ![screenshot](documentation/responsiveness/desktop_term.png) | ![screenshot](documentation/browser/firefox_term.png) | ![screenshot](documentation/browser/edge_term.png) | Works as expected |
| Rates History | ![screenshot](documentation/responsiveness/desktop_history.png) | ![screenshot](documentation/browser/firefox_rate.png) | ![screenshot](documentation/browser/edge_rate.png) | Works as expected |
| Add Trade | ![screenshot](documentation/responsiveness/desktop_addtrade.png) | ![screenshot](documentation/browser/firefox_addtrade.png) | ![screenshot](documentation/browser/edge_addtrade.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/desktop_404.png) | ![screenshot](documentation/responsiveness/desktop_500.png) | ![screenshot](documentation/responsiveness/desktop_404.png) | Works as expected |
| 500 | ![screenshot](documentation/responsiveness/desktop_500.png) | ![screenshot](documentation/responsiveness/desktop_500.png) | ![screenshot](documentation/responsiveness/desktop_500.png) | Works as expected |

---

No browser‑specific issues were identified. All pages behaved consistently across Chrome, Firefox, and Edge.

## 4. Data Integrity & Logic Testing

### 4.1 Market Data Logic

This section verifies the correctness, safety, and resilience of the “BlueGamma‑inspired” market data logic used throughout IRSQuant.

### Scenario A: The "6,000 Record" Load Test

*   **Test:** Loaded a high-density historical yield curve dataset (approx. 6,000 records) into the TermStructure view.
*   **Requirement:** The Apps data analysis views (dashboard, term structure etc) must remain stable and responsive when handling large volumes of market data.
*   **Observation:** The system successfully processed the full dataset; charts rendered correctly without layout shifts or "flickering."
*   **Performance Metrics (term structure):**
- Total Resource Weight: 807 kB (Uncompressed).
- Transferred Data: 11.9 kB (Optimized/Compressed).
- Style Load Time: 93 ms (Verified via Chrome DevTools).

*  **Status:** ✅ PASS
---

**Conclusion:** By cleaning duplicates and optimizing the transfer, 98.5% of the resource weight was handled via server-side efficiency, allowing the browser to achieve DOMContentLoaded in 3.26s even with heavy financial datasets. ![screenshot](documentation/tests/test_datacleaning.png)

### Scenario B: Front-End Stability Test
*   **Test:** Spoken "null" value into Chart.js data array via Console.
*   **Requirement:** Prevent crashes if market data is incomplete.
*   **Verification:**  To simulate a data gap without corrupting the production database, a DOM manipulation test was performed. This verified that the table layout remains stable and the "N/A" styling (aligned with the theme) is applied correctly.
*   **Outcome:** Terminal maintains layout; chart renders with a gap; no errors thrown.   **Status:** ✅ PASS
---

![screenshot](documentation/tests/test_dataNA.png)

### Scenario C: Attribution Links 
*   **Test:** Clicked "BlueGamma" attribution link in the footer.
*   **Requirement:** Must open in a new tab with `rel="noopener"` to prevent "Reverse Tabnabbing".
*   **Outcome:** Link opened safely in new tab. Original app remained active.
*   **Status:** ✅ PASS
---

![screenshot](documentation/tests/test_bg.png)

### 4.2 Trade Capture Validation

This table verifies that the IRSQuant terminal rejects logically impossible financial data.


| Test Case | Action| Expected Result | Actual Result | Status |
| --- | --- | --- | --- | --- |
| Negative Notional | Enter -1,000,000 in Notional field. |	Form validation error triggered. | "Ensure this value is greater than or equal to 0.01."	| ✅ PASS |
| Negative Start Delay | Enter -1 in Start Delay field. |	Form validation error triggered | "Ensure this value is greater than or equal to 0".	| ✅ PASS |
| Duplicate Trade id | Enter an existing Trade id. |  Database unique constraint prevents save. | "Trade with this Trade id already exists"	| ✅ PASS
| Financial Formatting | Enter 10000000 in the Notional field | @property formats decimal for UI. | Output $10,000,000| ✅ PASS


---

### 4.3 Automated Profile Syncing

The application uses django-allauth to enforce secure terminal access. In production, this is paired with a mandatory email verification code to prevent unauthorised entry.

| Feature |	Action | Expected Result | Status |
| --- |--- |--- |--- |
| SMTP Relay Security | Configured Gmail SMTP with 2-Step Verification & App Passwords. | Emails sent securely via an encrypted 16-digit token rather than a primary account password. | ✅ PASS |
| MFA Workflow | Mandatory 6-digit sign-in code sent to user email on login attempt. | Gmail SMTP relay successfully delivered the 6-digit verification code using the secure 16-digit App Password token. | ✅ PASS |
| Secure Authentication | Attempt to sign in with a new account | System triggers a verification email; user is blocked until code is entered. | ✅ PASS |
| Email Delivery | Check inbox for dclamp@yahoo.com | Email arrives from dclamp101@gmail.com containing the 6-digit code. |	✅ PASS |
| Code Validation | Enter incorrect/expired code |System rejects input and displays "Invalid code" warning. |	✅ PASS |
| Profile Persistence |	Update User model (e.g., change email).	| create_or_update_user_profile signal ensures the linked Profile remains in sync. | ✅ PASS
| Data Integrity | Delete a User from the Django Admin. | models.CASCADE (if set) removes the Profile; orphaned profiles are prevented.	| ✅ PASS

* **Manual Test:** Email Delivery Success

- Trigger: Sign-in attempt for dclamp@yahoo.com.
- Result: Verified that the Django-Allauth system successfully dispatched a verification email via the Gmail SMTP relay (dclamp101@gmail.com).

**Screenshot Evidence:**
- Insert Screenshot 1: ![screenshot](documentation/signin_code.png)The "Enter Sign-In Code" terminal interface.
- Insert Screenshot 2: ![screenshot](documentation/tests/test_dataNA.png)The actual verification email in your Yahoo inbox.

---

## 5. Business Logic & Data Privacy

These tests ensure that IRSQuant correctly isolates user data, aggregates financial metrics, and handles zero‑state scenarios safely.

| Feature | Action | Expected Result | Status |
| :--- | :--- | :--- | :--- |
| Privacy Check | Logged in as User B| Should NOT show User A's trades. | ✅ PASS |
| Aggregation | | Created 2 trades with same strategy. | Should group into one row. | ✅ PASS |
| Zero State | New user with 0 trades | NPV should be $0, no errors. | ✅ PASS |
| Public Access | Viewed 'Latest SOFR Date' | Should be visible to all users. | ✅ PASS |
| Data Ingestion| Set BLUEGAMMA_API_KEY to null/empty. | System should identify missing key and switch to local data. |	✅ PASS |
| Local Fallback | Ingest 6k market records. | market_data_test.json parsed. |	~1.1s (Verified via PowerShell)	| ✅ PASS|
| Portfolio Tagging | Outright Book ID | Added TRD-151 to two Outright trades.|Dashboard aggregates individual Outrights into a single portfolio row. |	✅ PASS |

---


## 6. Defensive Programming

Defensive programming ensures that the application handles invalid input, unexpected user behaviour, and system errors safely.



| Security Case	 | Action |	Actual Result |	Status |
| --- | --- | --- | --- |
| Invalid URL Handling | Navigated to /non-existent-link | Custom 404 template rendered with active navigation.| ✅ PASS|
| Server Fault Handling | Triggered via internal test route | Custom 500 template prevented exposure of raw code. | ✅ PASS|
| Unauthorised Access |	Visited Dashboard while logged out | Redirected: Anonymous session pushed to Login portal.|	✅ PASS|
| Data Isolation (CRUD) | Attempted to Edit/Delete another user's Trade ID | Forbidden: Request rejected via user.trades filtering. | ✅ PASS|
| Privileged Access	| Attempted /admin access with standard account	| Denied: Superuser credentials required for access.| ✅ PASS|
| MFA Gatekeeping |	Attempted to bypass code screen via direct URL | Redirect Loop: Access denied until 6-digit code verified.|	✅ PASS|
---

## Section 6.1  Stripe Security & Resilience

| Security Case	 | Action |	Actual Result |	Status |
| --- | --- | --- | --- |
| Signature Verification | Attempted to send a fake JSON payload to the Webhook URL. |	Rejected: System identified missing/invalid Stripe-Signature and returned a 400 error. |✅ PASS |
| Session Isolation	| Attempted to manually navigate to /success/ without a valid Stripe session. |	Blocked: View requires a session_id and redirects to Dashboard with a warning.| ✅ PASS|
| Webhook Failover | Simulated a server timeout during the payment callback. |	Resilient: Stripe retries the webhook; logic handles duplicate events via customer_id check.| ✅ PASS |
| Metadata Integrity | Modified the 'Price ID' in the browser console before checkout. |	Secured: The price is defined server-side in settings.py; client-side overrides are ignored. | ✅ PASS |
| Abandoned Checkout | Closed the payment tab before completing the transaction. | Handled: No is_subscriber flag updated; user remains on 'Basic' tier safely. | ✅ PASS |

---

### Stripe Screenshots

| Screenshot |	Purpose	| Where to get it|
| --- | --- | ---|
[Stripe Checkout]	| Proof of public key is connected. | The Stripe-hosted payment page showing your app's name. |
| [Success Redirect] | Proof of the "Return URL" logic.	 | Apps "Success" page after a test payment. |
| [Webhook 200 OK] | Critical Security Proof. |	The Stripe Dashboard (Test Mode) > Developers > Webhooks, showing a list of 200 status codes.|
---

## 7. Lighthouse Audit


Lighthouse was used to test Performance, Accessibility, Best Practices, and SEO on both mobile and desktop.
Mobile scores are naturally lower due to Heroku Eco dyno cold‑start behaviour.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Login | ![screenshot](documentation/lighthouse/mobile_login.png) | ![screenshot](documentation/lighthouse/desktop_login.png) ||
| Logout| ![screenshot](documentation/lighthouse/mobile_signout.png) | ![screenshot](documentation/lighthouse/desktop_signout.png) ||
| Subscription| ![screenshot](documentation/lighthouse/mobile_subscription.png) | ![screenshot](documentation/lighthouse/desktop_subscription.png) ||
| Dashboard|![screenshot](documentation/lighthouse/desktop_dashboard.png) | ![screenshot](documentation/lighthouse/desktop_dashboard.png) ||
| Blotter | ![screenshot](documentation/lighthouse/mobile_blotter.png) | ![screenshot](documentation/lighthouse/desktop_blotter.png) | Performance 88:Score impacted by Heroku Eco Dyno "Wake up" time|
| Analyser | ![screenshot](documentation/lighthouse/mobile_analyser.png) | ![screenshot](documentation/lighthouse/desktop_analyser.png) ||
| Term Structure | ![screenshot](documentation/lighthouse/mobile_termstructure.png) | ![screenshot](documentation/lighthouse/desktop_termstructure.png) ||
| Rate History | ![screenshot](documentation/lighthouse/mobile_history.png) | ![screenshot](documentation/lighthouse/desktop_history.png) ||
| Add Trade | ![screenshot](documentation/lighthouse/mobile_addtrade.png) | ![screenshot](documentation/lighthouse/mobile_addtrade.png) ||
| 404 | ![screenshot](documentation/lighthouse/mobile_404.png) | ![screenshot](documentation/lighthouse/desktop_404.png) |Tested using trap door URL|
| 500 | ![screenshot](documentation/lighthouse/mobile_500.png) | ![screenshot](documentation/lighthouse/desktop_500.png) |Tested using trap door URL|
---


## 8. User Story Testing

### Features Mapped to User Stories ###

Each implemented feature was tested against the original User Stories to ensure that the application meets the needs of its intended users. The table below maps each user story to the corresponding feature and outcome.

| Target | Expectation (User Story) | Outcome | Screenshot |
| --- | --- | --- | --- |
| User | I want to register an account so that I can access platform features | Users can register via Django Allauth and gain access to authenticated areas | ![screenshot](documentation/responsiveness/desktop_signup.png) |
| User | I want to securely log in and out so that my data is protected | Django Allauth provides secure session‑based authentication |![screenshot](documentation/responsiveness/desktop_signin.png) |
| User | I want to upgrade to Pro so that I can access advanced features | Stripe subscription system enables secure payments and upgrades | ![screenshot](documentation/responsiveness/desktop_subscription.png) |
| Pro User | I want a payment confirmation email so that I have a record | Automated confirmation email sent after successful Stripe transaction |![screenshot](documentation/responsiveness/desktop_nin.png) |
| Pro User | I want a central dashboard so that I can quickly access key features | Dashboard displays analytics, navigation shortcuts, and account status | ![screenshot](documentation/responsiveness/desktop_dashboard.png) |
| Pro User | I want to view yield curve charts so that I can analyse the swaps market | Analysis board displays current zero and par curves |![screenshot](documentation/responsiveness/desktop_analyser.png) |
| User | I want to view implied forward curves to analyse future expectations | Interactive charts show implied 1‑year forward rate paths | ![screenshot](documentation/responsiveness/laptop_analyser.png) |
| User | I want to view historical rate distributions | Histogram charts display historical rate behaviour | ![screenshot](documentation/responsiveness/desktop_history.png) |
| Pro User | I want to view all my trades so that I can manage my portfolio | Dashboard lists all user trades with MTM and key metrics | ![screenshot](documentation/responsiveness/desktop_dashboard.png) |
| User | I want to add trades so that I can build a portfolio | Validated forms allow users to input new trades | ![screenshot](documentation/responsiveness/desktop_addtrade.png)|
| Pro User | I want to see MTM values so that I can track performance | Backend logic calculates MTM dynamically using current market data |![screenshot](documentation/responsiveness/desktop_dashboard.png) |
| Pro User | I want exclusive access to advanced tools | Subscription status controls access to restricted features | ![screenshot](documentation/responsiveness/desktop_dashboard.png) |
| Site Owner | I want to manage users and trades | Django Admin provides full CRUD access to all models |![screenshot](documentation/responsiveness/desktop_signin.png) |
| User | I want clear 404 and 500 pages so that I can recover from issues | Custom error pages improve UX during failures | ![screenshot](documentation/responsiveness/desktop_404.png) |
||||![screenshot](documentation/responsiveness/desktop_500.png)|


## 9. Automated Testing

### 9.1 Django Unittest Framework

Automated tests were written using Django’s built‑in unittest framework to verify:

- Model behaviour

- View accessibility

- Form validation

- Calculation logic


### **Running Tests**

```powershell
python manage.py test workspace

### **Automated Testing Results** ### 
*Date: April 09, 2026*

The application's core logic was verified using Django's `unittest` suite. 
All critical paths (Models, Views, Forms) passed successfully.

**Command:**
`python manage.py test workspace`

**Output:**

Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).

Ran 5 tests in 7.928s

OK
```
These tests confirm that the core logic of the application behaves as expected.
In a production environment, a more extensive suite would be implemented.


### 9.2 Coverage Testing

Coverage was used to measure how much of the codebase is executed during testing.

pip3 install coverage
pip3 freeze --local > requirements.txt
coverage run --omit="*/site-packages/*,*/migrations/*,*/__init__.py,env.py,.env" manage.py test
coverage report
coverage html
python -m http.server


Below are the results from the full coverage report.

![screenshot](documentation/automation/html-coverage.png)


## 10. Known Bugs, Issues & Fixes



### 10.1 Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/DavidClamp/project-swaps?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/DavidClamp/project-swaps/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/DavidClamp/project-swaps/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/DavidClamp/project-swaps/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

| Issue | Resolution|
| --- | --- |
| A faint white line appeared between "Login" and "Sign Up" buttons on Desktop. | Removed border classes entirely and replaced with `<hr class="d-lg-none">` to show divider only on mobile.|
| Yield Curve chart “wobbled” during window resize. | Wrapped canvas in a fixed‑size container `position: relative; height: 450px; width: 100%;`. |
| Heading Level Skip |	Validator flagged an h6 following an h1. Corrected hierarchy to use h2 with .h6 styling for accessibility compliance.|
|API Cost Barrier	Real-time API access is restricted to paid enterprise tiers.| Implemented a Local Seed Data mechanism using a high-density JSON file to simulate real-world yield curves without recurring costs.|
| Integrity Error (duplicate key) on new user signup. |Refactored signals.py to use a single consolidated receiver with get_or_create logic to handle Allauth race conditions. |
---

### 10.2 Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/DavidClamp/project-swaps?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/DavidClamp/project-swaps/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/DavidClamp/project-swaps/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/bugs/gh-issues-open.png)

### 10.3  Known Issues

| Issue | Screenshot |
| --- | --- |
| No known issues at this time| |

Although no issues are currently known, further testing may reveal additional edge cases.

