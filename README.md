# QA Automation Project – SauceDemo

## 📌 Overview
This project demonstrates structured manual and automated testing of the SauceDemo e-commerce application.

The goal was to validate core user workflows and automate high-priority scenarios using Selenium and Pytest.

---

## 🧪 Manual Testing
- Designed and executed 30+ functional test cases
- Covered Login, Cart, and Checkout modules
- Identified and documented 1 business logic defect (checkout allowed with empty cart)
- Classified defects by severity and priority

---

## 🤖 Automation Testing

Automated core end-to-end workflows using:

- Python
- Selenium WebDriver
- Pytest
- WebDriverWait (Explicit Waits)
- ChromeDriverManager

### Automated Test Scenarios

- Valid Login
- Invalid Login
- Add Item to Cart
- Complete Checkout Flow

---

## 🏗 Project Structure


QA-Automation-SauceDemo/
│
├── tests/
│ ├── conftest.py
│ ├── test_login.py
│ └── test_cart.py
│
├── requirements.txt
└── README.md

## ▶️ How To Run

1. Clone repository:

git clone <repo-link>

2. Install dependencies:
  
3. Run tests:
   pytest


---

## 🎯 Key Learnings

- Designing structured manual test cases
- Writing reusable test fixtures using Pytest
- Handling synchronization using explicit waits
- Debugging Selenium element interaction issues
- Building a scalable automation structure



