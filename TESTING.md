# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Testing Strategy & Methodology

The testing strategy for **IRSQuant** utilises a "Hybrid" approach, combining automated unit tests for critical financial calculations (Data Integrity) with rigorous manual usability testing for the UI/UX (Responsiveness).

**Testing Phases:**
1.  **Validator Auditing:** Ensuring strict code compliance (W3C HTML, Jigsaw CSS, CI Python Linter).
2.  **Responsive Stress Testing:** Verifying the "Hybrid Navbar" behavior across 4 specific breakpoints.
3.  **Logical Data Testing:** Verifying the "BlueGamma" data cleaning protocols and trade capture logic.
4.  **Lighthouse Auditing:** Performance and Accessibility scoring (targeting WCAG 2.1 AA standards).

---

## 1. Code Validation

### HTML Validation
I have used the [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

**Methodology:**
Since the project uses Django Template Language (Jinja syntax like `{% url %}`), direct URI validation fails on protected pages. I utilized the **"View Source"** method:
1.  Navigate to the rendered page in the browser.
2.  Right-click > "View Page Source".
3.  Copy the raw compiled HTML.
4.  Paste into the W3C Validator (Validate by Input).

| Directory | File | Status | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| templates | [base.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/footer.html) | ✅ PASS  | ![screenshot](documentation/validation/html-templates-footer.png) | ⚠️ Notes (if applicable) |
| templates | [footer.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/footer.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-templates-footer.png) | ⚠️ Notes (if applicable) |
| templates | [navbar.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/navbar.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-templates-navbar.png) | ⚠️ Notes (if applicable) |
| workspace | [404.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/404.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-workspace-404.png) | ⚠️ Notes (if applicable) |
| workspace | [500.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/500.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-workspace-500.png) | ⚠️ Notes (if applicable) |
| workspace | [add_trade.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/add_trade.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-workspace-add_trade.png) | ⚠️ Notes (if applicable) |
| workspace | [analyser.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/analyser.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-workspace-analyser.png) | ⚠️ Notes (if applicable) |
| workspace | [blotter.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/blotter.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-workspace-blotter.png) | ⚠️ Notes (if applicable) |
| workspace | [curve_bars.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/curve_bars.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-workspace-curve_bars.png) | ⚠️ Notes (if applicable) |
| workspace | [dashboard.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/dashboard.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-workspace-dashboard.png) | ⚠️ Notes (if applicable) |
| workspace | [delete_confirm.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/delete_confirm.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-workspace-delete_confirm.png) | ⚠️ Notes (if applicable) |
| workspace | [edit_trade.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/edit_trade.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-workspace-edit_trade.png) | ⚠️ Notes (if applicable) |
| workspace | [histogram.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/histogram.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-workspace-histogram.png) | ⚠️ Notes (if applicable) |
| workspace | [payment_cancelled.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/payment_cancelled.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-workspace-payment_cancelled.png) | ⚠️ Notes (if applicable) |
| workspace | [payment_success.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/payment_success.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-workspace-payment_success.png) | ⚠️ Notes (if applicable) |
| workspace | [plans.html](https://github.com/DavidClamp/project-swaps/blob/main/workspace/templates/workspace/plans.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-workspace-plans.png) | ⚠️ Notes (if applicable) |
| account | [login.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/account/login.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-templates-login.png) | ⚠️ Notes (if applicable) |
| account | [logout.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/account/logout.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-templates-logout.png) | ⚠️ Notes (if applicable) |
| account | [password_reset.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/account/password_reset.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-templates-password_reset.png) | ⚠️ Notes (if applicable) |
| account | [signup.html](https://github.com/DavidClamp/project-swaps/blob/main/templates/account/signup.html) | ⚠️ Link (if applicable) | ![screenshot](documentation/validation/html-templates-signup.png) | ⚠️ Notes (if applicable) |


### CSS Validation
I have used the [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/) to validate my custom CSS.

| Directory | File | Status | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [style.css](https://github.com/DavidClamp/project-swaps/blob/main/static/css/style.css) | ✅ PASS | ![screenshot](documentation/validation/css-static-style.png) | Validated Root Variables (`--ua-gold`) and vendor prefixes. |


### Python Validation
All Python code was checked using the **CI Python Linter** (PEP8 standard).

**IMPORTANT**: `E501 line too long` errors

I have strived to fix all Python lines that are too long (>80 characters). In some cases I cannot break the lines [*without breaking the functionality*].

| Directory | File | URL | Screenshot | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| 
| Root | [manage.py](https://github.com/DavidClamp/project-swaps/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) | ⚠️ Notes (if applicable) |
| swapanalyser | [settings.py](https://github.com/DavidClamp/project-swaps/blob/main/swapanalyser/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/swapanalyser/settings.py) | ![screenshot](documentation/validation/py-swapanalyser-settings.png) | Ignored "Line too long" for AUTH_PASSWORD_VALIDATORS (Standard Django Exception). |
| swapanalyser | [urls.py](https://github.com/DavidClamp/project-swaps/blob/main/swapanalyser/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/swapanalyser/urls.py) | ![screenshot](documentation/validation/py-swapanalyser-urls.png) | ⚠️ Notes (if applicable) |
| workspace | [admin.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/admin.py) | ![screenshot](documentation/validation/py-workspace-admin.png) | ⚠️ Notes (if applicable) |
| workspace | [checkout_views.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/checkout_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/checkout_views.py) | ![screenshot](documentation/validation/py-workspace-checkout_views.png) | ⚠️ Notes (if applicable) |
| workspace | [choices.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/choices.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/choices.py) | ![screenshot](documentation/validation/py-workspace-choices.png) | ⚠️ Notes (if applicable) |
| workspace | [data_handler.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/data_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/data_handler.py) | ![screenshot](documentation/validation/py-workspace-data_handler.png) | ⚠️ Notes (if applicable) |
| workspace | [forms.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/forms.py) | ![screenshot](documentation/validation/py-workspace-forms.png) | ⚠️ Notes (if applicable) |
| workspace | [models.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/models.py) | ![screenshot](documentation/validation/py-workspace-models.png) | ⚠️ Notes (if applicable) |
| workspace | [tests.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/tests.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/tests.py) | ![screenshot](documentation/validation/py-workspace-tests.png) | ⚠️ Notes (if applicable) |
| workspace | [utils.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/utils.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/utils.py) | ![screenshot](documentation/validation/py-workspace-utils.png) | ⚠️ Notes (if applicable) |
| workspace | [views.py](https://github.com/DavidClamp/project-swaps/blob/main/workspace/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/DavidClamp/project-swaps/main/workspace/views.py) | ![screenshot](documentation/validation/py-workspace-views.png) | ⚠️ Notes (if applicable) |

---

## 2. Responsive & Theme Testing

### Responsiveness
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


I've tested my deployed project on multiple browsers to check for compatibility issues.

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

## 4. Data Integrity & Logic Testing

This section verifies the "BlueGamma" inspired market data logic.

### Scenario A: The "6,000 Record" Load Test
*   **Test:** Loaded the full historical yield curve JSON dataset into the `TermStructure` view.
*   **Requirement:** Dashboard must render in < 200ms without flickering.
*   **Observation:** Duplicate removal script successfully reduced payload by ~12%. Charts rendered instantly.
*   **Status:** ✅ PASS

### Scenario B: The "KeyError" Safety Net
*   **Test:** Intentionally introduced a JSON record with a missing `mid_rate` key to simulate a feed outage.
*   **Logic:** The Django template filter `|default:"N/A"` intercepted the error.
*   **Outcome:** Page loaded without crashing; missing data was gracefully marked as "N/A".
*   **Status:** ✅ PASS

### Scenario C: Attribution Links (Legal)
*   **Test:** Clicked "BlueGamma" link in Footer.
*   **Requirement:** Must open in `_blank` tab with `rel="noopener"` to prevent "Reverse Tabnabbing" and user loss.
*   **Outcome:** Link opened safely in new tab. Original app remained open.
*   **Status:** ✅ PASS

## 5. Business Logic & Data Privacy

**Objective:** Verify that the Dashboard correctly aggregates financial data WITHOUT leaking information between users.

| Component | Test Case | Action | Expected Result | Actual Result |
| :--- | :--- | :--- | :--- | :--- |
| **Dashboard** | **Privacy Check** | Logged in as User B. Checked Total NPV. | Should NOT include User A's trades. | **PASS** (Only showed User B's data) |
| **Aggregation** | **Strategy Grouping** | Created 2 trades with same 'Strategy' tag. | Dashboard should group them into one row. | **PASS** (Grouped correctly) |
| **KPI Calculation** | **Zero State** | Created new user with 0 trades. | NPV should be $0, no crashes. | **PASS** (Handled safely) |
| **Market Data** | **Public Access** | Checked 'Latest SOFR Date' on Dashboard. | Should show date regardless of user. | **PASS** (Global data is accessible) |

---

## 4. Lighthouse Audit


I've tested my project using the Lighthouse Audit tool to test Performance, Accessibility, Best Practices, and SEO. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

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

⚠️ INSTRUCTIONS ⚠️

Defensive programming (defensive design) is extremely important! When building projects that accept user inputs or forms, you should always test the level of security for each form field. Examples of this could include (but not limited to):


- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

⚠️ --- END --- ⚠️

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |
| 500 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## 6. User Story Testing

### Features Mapped to User Stories ###

The table below demonstrates how each implemented feature fulfils specific user needs identified in the User Stories section.
| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | ---|
| User | I want to register an account so that I can access platform features | Users can create an account using Django Allauth, enabling access to authenticated areas ||
| User | I want to securely log in and out so that my data is protected | Authentication system ensures secure session management||
| User | Stripe Subscription |As a user, I want to upgrade to Pro so that I can access advanced features | Stripe integration enables Stripe-powered subscription payments |
| Pro User |Payment Confirmation Email | As a Pro user, I want confirmation of my payment so that I have a record | Automated email is triggered after successful Stripe transaction |
| Pro User | I want a central dashboard so that I can quickly access key features | Dashboard provides an overview of analytics, navigation, and account status ||
| Pro User | I want to view yield curve charts so that I can analyse the swaps market | Analysis board displays current market zero and par curves ||
| Pro User |Implied Forward Rate Curve Visualisation | As a user, I want to view forward yield curve to analyse implied path | Interactive charts display current implied path of 1-year rates |
| Pro User | Rate Distribution Charts | As a user, I want to view historical distributions so that I can understand market behaviour | Histogram charts present historical rate data clearly  |
| Pro User |Trade Blotter | As a Pro user, I want to view all my trades so that I can manage my portfolio | Displays all user trades with key metrics such as MTM |
| Pro User | Add Trade Functionality | As a Pro user, I want to add trades so that I can build a portfolio | Users can input trade details via validated forms |
| Pro User | I want to see MTM values so that I can track performance | Backend calculations provide dynamically calculated portfolio valuation based on current dataset |
| Pro User | I want exclusive access to advanced tools | Subscription status controls access to restricted features |
| Site Owner | I want to manage users and trades so that I can manage users and trade data | Django admin panel allows full database management                                       |
| User | I want clear 404 and 500 error pages so that I can recover from issues | Custom error pages improve user experience during failures                               |
---


## Automated Testing

## Testing Documentation

## 1. Automated Testing (Django & Unittest)
The application uses Django's built-in `unittest` framework to verify data integrity, view accessibility, and calculation logic.

### **Running Tests**
To execute the automated test suite, I ran the following command in the terminal:
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

> [!NOTE]  
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### 7. Python (Unit Testing)


I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit="*/site-packages/*,*/migrations/*,*/__init__.py,env.py,.env" manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python -m http.server`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

⚠️ INSTRUCTIONS ⚠️

Use this section to list any known issues you ran into while writing your Python unit tests. Remember to include screenshots (where possible), and a solution to the issue (if known). This can be used for both "fixed" and "unresolved" issues. Remove this sub-section entirely if you somehow didn't run into any issues while working with your tests.

⚠️ --- END --- ⚠️

## 8. Known Bugs & Fixes

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/DavidClamp/project-swaps?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/DavidClamp/project-swaps/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/DavidClamp/project-swaps/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/DavidClamp/project-swaps/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)


### The "Phantom Border" Bug
*   **Issue:** A faint white line appeared between "Login" and "Sign Up" buttons on Desktop screens.
*   **Cause:** I initially used `border-top` on the mobile menu container for separation, and tried to remove it with `border-lg-0`. Bootstrap **does not** have a `border-lg-0` class, so the border remained visible on Desktop.
*   **Fix:** Removed the border classes entirely. I implemented a `<hr class="d-lg-none">` element. This divider line is explicitly hidden on large screens using display utilities, ensuring it **only** appears on mobile.
*   **Status:** ✅ **FIXED**

### Chart.js Resize Jitter
*   **Issue:** On resizing the window, the Yield Curve chart would momentarily "wobble."
*   **Fix:** Added a container `div` with `position: relative; height: 450px; width: 100%;` to constrain the canvas aspect ratio.
*   **Status:** ✅ **FIXED**

### Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/DavidClamp/project-swaps?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/DavidClamp/project-swaps/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/DavidClamp/project-swaps/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.
