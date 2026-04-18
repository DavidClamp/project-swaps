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
| templates | [base.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/footer.html) | ✅ PASS  | ![screenshot](documentation/validation/html-templates-footer.png) | No issues |
| templates | [footer.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/footer.html) | ⚠️Minor | ![screenshot](documentation/validation/html-templates-footer.png) | Minor warnings (template tags ignored by validator) || templates | [navbar.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/navbar.html) | ⚠️Minor | ![screenshot](documentation/validation/html-templates-footer.png) | Minor warnings |
Templates | [navbar.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/navbar.html) | ⚠️Minor | ![screenshot](documentation/validation/html-templates-navbar.png) | Minor Warnings |
| workspace | [404.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/404.html) | ⚠️ Minor| ![screenshot](documentation/validation/html-workspace-404.png) | Template‑tag related warnings |
| workspace | [500.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/500.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-workspace-500.png) | Template‑tag related warnings |
| workspace | [add_trade.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/add_trade.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-workspace-add_trade.png) | Minor warnings |
| workspace | [analyser.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/analyser.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-workspace-analyser.png) | Minor warnings |
| workspace | [blotter.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/blotter.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-workspace-blotter.png) | Minor warnings |
| workspace | [curve_bars.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/curve_bars.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-workspace-curve_bars.png) | Minor warnings |
| workspace | [dashboard.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/dashboard.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-workspace-dashboard.png) | Minor warnings |
| workspace | [delete_confirm.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/delete_confirm.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-workspace-delete_confirm.png) | Minor warnings |
| workspace | [edit_trade.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/edit_trade.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-workspace-edit_trade.png) | Minor warnings |
| workspace | [histogram.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/histogram.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-workspace-histogram.png) | Minor warnings |
| workspace | [payment_cancelled.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/payment_cancelled.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-workspace-payment_cancelled.png) | Minor warnings |
| workspace | [payment_success.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/payment_success.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-workspace-payment_success.png) | Minor warnings |
| workspace | [plans.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/plans.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-workspace-plans.png) | Minor warnings |
| account | [login.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/account/login.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-templates-login.png) | Minor warnings |
| account | [logout.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/account/logout.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-templates-logout.png) | Minor warnings |
| account | [password_reset.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/account/password_reset.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-templates-password_reset.png) | Minor warnings |
| account | [signup.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/account/signup.html) | ⚠️ Minor | ![screenshot](documentation/validation/html-templates-signup.png) | Minor warnings |

All warnings were related to Django template syntax and not actual HTML errors.

---

### CSS Validation
I have used the [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/) to validate my custom CSS.

| Directory | File | Status | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [style.css](https://github.com/DavidClamp/project-swaps/blob/main/static/css/style.css) | ✅ PASS | ![screenshot](documentation/validation/css-static-style.png) | All root variables and vendor prefixes validated successfully vendor prefixes. |


### Python Validation
All Python code was checked using the **CI Python Linter** (PEP8 standard).

**NOTE**: `E501 line too long` 

Where possible, long lines were refactored. Some Django‑generated or settings‑related lines cannot be shortened without breaking functionality.


| Directory | File | URL | Screenshot | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| 
| Root | [manage.py](https://github.com/DavidClamp/project-swaps/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) | ⚠️ | Minor warnings |
| swapanalyser | [settings.py](https://github.com/DavidClamp/project-swaps/blob/main/swapanalyser/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/swapanalyser/settings.py) | ![screenshot](documentation/validation/py-swapanalyser-settings.png) | ⚠️| Long lines in AUTH_PASSWORD_VALIDATORS (standard Django exception) |
| swapanalyser | [urls.py](https://github.com/DavidClamp/project-swaps/blob/main/swapanalyser/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/swapanalyser/urls.py) | ![screenshot](documentation/validation/py-swapanalyser-urls.png) | ⚠️ | Minor warnings |
| workspace | [admin.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/admin.py) | ![screenshot](documentation/validation/py-workspace-admin.png) | ⚠️ | Minor warnings |
| workspace | [checkout_views.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/checkout_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/checkout_views.py) | ![screenshot](documentation/validation/py-workspace-checkout_views.png) | ⚠️ | Minor warnings |
| workspace | [choices.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/choices.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/choices.py) | ![screenshot](documentation/validation/py-workspace-choices.png) | ⚠️| Minor warnings |
| workspace | [data_handler.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/data_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/data_handler.py) | ![screenshot](documentation/validation/py-workspace-data_handler.png) | ⚠️ | Minor warnings |
| workspace | [forms.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/forms.py) | ![screenshot](documentation/validation/py-workspace-forms.png) | ⚠️ | Minor warnings |
| workspace | [models.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/models.py) | ![screenshot](documentation/validation/py-workspace-models.png) | ⚠️ | Minor warnings |
| workspace | [tests.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/tests.py) | ![screenshot](documentation/validation/py-workspace-tests.png) | ⚠️ | Minor warnings |
| workspace | [utils.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/utils.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/utils.py) | ![screenshot](documentation/validation/py-workspace-utils.png) | ⚠️ | Minor warnings |
| workspace | [views.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/views.py) | ![screenshot](documentation/validation/py-workspace-views.png) | ⚠️ | Minor warnings |

---

## 2. Responsive & Theme Testing

### Responsiveness

Responsiveness was tested across mobile, tablet and desktop breakpoints.
I've tested my deployed project to check for responsiveness issues.

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
| 404 | ![screenshot](documentation/responsiveness/desktop_404.png) | ![screenshot](documentation/browsers/firefox-bag.png) | ![screenshot](documentation/browsers/safari-bag.png) | Works as expected |
| 500 | ![screenshot](documentation/responsiveness/desktop_500.png) | ![screenshot](documentation/browsers/firefox-bag.png) | ![screenshot](documentation/browsers/safari-bag.png) | Works as expected |

No browser‑specific issues were identified. All pages behaved consistently across Chrome, Firefox, and Edge.

## 4. Data Integrity & Logic Testing

This section verifies the correctness, safety, and resilience of the “BlueGamma‑inspired” market data logic used throughout IRSQuant.

### Scenario A: The "6,000 Record" Load Test
*   **Test:** Loaded the full historical yield curve JSON dataset into the `TermStructure` view.
*   **Requirement:** Dashboard must render in < 200ms without flickering.
*   **Observation:** Duplicate removal script successfully reduced payload by ~12%. Charts rendered instantly.
*   **Status:** ✅ PASS

### Scenario B: The "KeyError" Safety Net
*   **Test:** Intentionally introduced a JSON record with a missing `mid_rate` key.
*   **Logic:** The Django template filter `|default:"N/A"` prevented a crash.
*   **Outcome:** Page loaded normally; missing values displayed as "N/A".
*   **Status:** ✅ PASS

### Scenario C: Attribution Links (Legal)
*   **Test:** Clicked "BlueGamma" attribution link in the footer.
*   **Requirement:** Must open in a new tab with `rel="noopener"` to prevent "Reverse Tabnabbing".
*   **Outcome:** Link opened safely in new tab. Original app remained active.
*   **Status:** ✅ PASS

## 5. Business Logic & Data Privacy

These tests ensure that IRSQuant correctly isolates user data, aggregates financial metrics, and handles zero‑state scenarios safely.


| Component | Test Case | Action | Expected Result | Actual Result |
| :--- | :--- | :--- | :--- | :--- |
| **Dashboard** | **Privacy Check** | Logged in as User B| Should NOT show User A's trades. | ✅ PASS |
| **Aggregation** | **Strategy Grouping** | Created 2 trades with same strategy | Should group into one row. | ✅ PASS |
| **KPI Calculation** | **Zero State** | New user with 0 trades | NPV should be $0, no errors. | ✅ PASS |
| **Market Data** | **Public Access** | Viewed 'Latest SOFR Date' | Should be visable to all usera. | ✅ PASS |

---
## 4. Lighthouse Audit


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
## 5. Defensive Programming

Defensive programming ensures that the application handles invalid input, unexpected user behaviour, and system errors safely.

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| 404 Error Page | Should display custom 404 page for invalid URLs | Navigated to ``/test`` | Custom 404 displayed | screenshot |
| 500 Error Page | Should display custom 500 page on server error | Triggered via trap‑door URL | Custom 500 displayed | screenshot |


## 6. User Story Testing

### Features Mapped to User Stories ###

Each implemented feature was tested against the original User Stories to ensure that the application meets the needs of its intended users. The table below maps each user story to the corresponding feature and outcome.

| Target | Expectation (User Story) | Outcome | Screenshot |
| --- | --- | --- | --- |
| User | I want to register an account so that I can access platform features | Users can register via Django Allauth and gain access to authenticated areas | — |
| User | I want to securely log in and out so that my data is protected | Django Allauth provides secure session‑based authentication | — |
| User | I want to upgrade to Pro so that I can access advanced features | Stripe subscription system enables secure payments and upgrades | — |
| Pro User | I want a payment confirmation email so that I have a record | Automated confirmation email sent after successful Stripe transaction | — |
| Pro User | I want a central dashboard so that I can quickly access key features | Dashboard displays analytics, navigation shortcuts, and account status | — |
| Pro User | I want to view yield curve charts so that I can analyse the swaps market | Analysis board displays current zero and par curves | — |
| Pro User | I want to view implied forward curves to analyse future expectations | Interactive charts show implied 1‑year forward rate paths | — |
| Pro User | I want to view historical rate distributions | Histogram charts display historical rate behaviour | — |
| Pro User | I want to view all my trades so that I can manage my portfolio | Blotter lists all user trades with MTM and key metrics | — |
| Pro User | I want to add trades so that I can build a portfolio | Validated forms allow users to input new trades | — |
| Pro User | I want to see MTM values so that I can track performance | Backend logic calculates MTM dynamically using current market data | — |
| Pro User | I want exclusive access to advanced tools | Subscription status controls access to restricted features | — |
| Site Owner | I want to manage users and trades | Django Admin provides full CRUD access to all models | — |
| User | I want clear 404 and 500 pages so that I can recover from issues | Custom error pages improve UX during failures | — |



## 7. Automated Testing

### 7.1 Django Unittest Framework

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


### 7.2 Coverage Testing

Coverage was used to measure how much of the codebase is executed during testing.

pip3 install coverage
pip3 freeze --local > requirements.txt
coverage run --omit="*/site-packages/*,*/migrations/*,*/__init__.py,env.py,.env" manage.py test
coverage report
coverage html
python -m http.server


Below are the results from the full coverage report.

![screenshot](documentation/automation/html-coverage.png)


## 8. Known Bugs & Fixes



### 8.1 Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/DavidClamp/project-swaps?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/DavidClamp/project-swaps/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/DavidClamp/project-swaps/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/DavidClamp/project-swaps/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)


### The "Phantom Border" Bug
*   **Issue:** A faint white line appeared between "Login" and "Sign Up" buttons on Desktop.
*   **Cause:**  `border-top` was applied on mobile, but `border-lg-0` does not exist in Bootstrap.
*   **Fix:** Removed border classes entirely and replaced with `<hr class="d-lg-none">` to show divider only on mobile.
*   **Status:** ✅ **FIXED**

### Chart.js Resize Jitter
*   **Issue:** Yield Curve chart “wobbled” during window resize.
*   **Fix:** Wrapped canvas in a fixed‑size container `position: relative; height: 450px; width: 100%;`.
*   **Status:** ✅ **FIXED**

### 8.2 Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/DavidClamp/project-swaps?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/DavidClamp/project-swaps/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/DavidClamp/project-swaps/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/bugs/gh-issues-open.png)

### 8.3  Known Issues

| Issue | Screenshot |
| --- | --- |
| No known issues at this time| |

Although no issues are currently known, further testing may reveal additional edge cases.

