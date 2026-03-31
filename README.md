# Saucelabs Mobile QA Automation

![Appium Tests](https://github.com/revanth00744-beep/saucelabs-mobile-qa/actions/workflows/appium.yml/badge.svg)

Mobile test automation suite for the Sauce Labs Android sample app.

## Stack
- Python + Appium 2 + UiAutomator2
- pytest + pytest-html
- Page Object Model with BasePage
- GitHub Actions CI/CD
- BrowserStack App Automate (Pixel 7, Android 13)

## Test Coverage (21 tests)
- Login: valid login, locked out, wrong password, empty fields (2)
- Products: page load, sorting (4 options), add to cart, swipe gesture
- Cart: page load, item display, continue shopping
- Checkout: end-to-end success, order total, missing fields (3), cancel

## Run locally
Start your Android emulator and Appium server first, then:

- pip install -r requirements.txt
- pytest

## CI/CD
On every push to main, tests run automatically on a real Pixel 7
device via BrowserStack App Automate.
