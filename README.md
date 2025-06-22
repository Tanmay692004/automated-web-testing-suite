# Automated Web Testing Suite

![CI](https://github.com/Tanmay692004/automated-web-testing-suite/actions/workflows/pytest.yml/badge.svg)

A Selenium + Python test suite that runs automatically on every push using GitHub Actions.


This project automates key test cases for an e-commerce website using Selenium and Python.

## 🔧 Tech Stack
- Python 3
- Selenium WebDriver
- TestNG-style structure (pytest)
- GitHub Actions for CI
- HTML Test Reports

## ✅ Features Tested
- Login and logout
- Product search
- Add to cart
- Checkout flow
- Error validations

## 🚀 How to Run

```bash
pip install -r requirements.txt
pytest test_cases/ --html=report.html
