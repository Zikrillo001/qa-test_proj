Zo‘r. Unda README’ni oddiy “instruction file” emas, balki **professional portfolio hujjati** sifatida yozamiz. Bu intervyuda ochib ko‘rsatiladigan darajada bo‘ladi.

Quyidagini to‘liq `README.md` ga qo‘ying.

---

# AutomationExercise – QA Automation Portfolio (Python)

Production-style QA automation framework built for
[https://automationexercise.com](https://automationexercise.com)

This project demonstrates **Middle-level QA Engineering skills**, including:

* UI automation (Playwright)
* API testing (requests)
* UI ↔ API correlation
* Cross-browser execution
* Test architecture design
* CI/CD integration
* HTML reporting & failure artifacts

---

## 🔹 Tech Stack (2026 Market-Oriented)

**UI Automation**

* Playwright (Python)
* Pytest

**API Testing**

* requests
* JSON validation

**Architecture**

* Page Object Model
* Layered structure (UI / API / Core / Config)
* Environment configuration via `.env`

**Quality & Tooling**

* ruff (linting)
* black (formatting)
* pytest markers (smoke / regression)

**CI/CD**

* GitHub Actions
* Matrix execution (chromium / firefox / webkit)
* HTML reports uploaded as artifacts

---

## 🔹 Project Structure

```
automationexercise/
│
├── src/
│   ├── api/            # API client layer
│   ├── config/         # Environment settings
│   ├── core/           # Base page & common utilities
│   ├── pages/          # Page Object classes
│
├── tests/
│   ├── ui/             # UI test cases
│   ├── api/            # API test cases
│   ├── e2e/            # UI ↔ API correlation tests
│
├── reports/            # Generated HTML reports (gitignored)
├── .github/workflows/  # CI configuration
├── pytest.ini
├── .env.example
└── README.md
```

---

## 🔹 Test Strategy (Design Rationale)

This project follows a simplified **test pyramid approach**:

* **API Tests**
  Fast validation of backend contracts and negative scenarios.

* **UI Tests (Smoke / Regression)**
  Critical business flows:

  * Login
  * Registration
  * Add to Cart
  * Checkout
  * Negative validation cases

* **UI ↔ API Correlation Tests**
  Ensures frontend data is consistent with backend payloads.

This demonstrates system-level thinking beyond UI-only automation.

---

## 🔹 Key Features Implemented

✔ Cross-browser support (Chromium / Firefox / WebKit)
✔ Deterministic test handling (xfail strategy for unstable data)
✔ HTML reporting
✔ Automatic screenshot capture on failure
✔ Environment-based configuration
✔ Clean Page Object architecture

---

## 🔹 Local Setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -U pip
pip install playwright pytest pytest-html requests python-dotenv ruff black faker
playwright install
```

---

## 🔹 Running Tests

### Smoke Suite

```bash
pytest -m smoke
```

### Regression Suite

```bash
pytest -m regression
```

### Cross-Browser Execution (Windows CMD)

```bash
set BROWSER=chromium && pytest -m smoke
set BROWSER=firefox && pytest -m smoke
set BROWSER=webkit && pytest -m smoke
```

---

## 🔹 Generate HTML Report

```bash
pytest --html=reports/all.html --self-contained-html
```

Reports are automatically generated in CI and uploaded as artifacts.

---

## 🔹 Environment Configuration

Create `.env` file from `.env.example`

Example:

```
BASE_URL=https://automationexercise.com
HEADLESS=true
BROWSER=chromium
```

---

## 🔹 CI/CD Pipeline

On every push:

* Lint & format validation
* Test execution in 3 browsers (matrix strategy)
* HTML report generation
* Artifact upload (including screenshots)

This simulates real production QA workflow.

---

## 🔹 What This Project Demonstrates

This repository is not just test scripts — it demonstrates:

* Automation architecture design
* Risk-based test coverage
* System-level validation (UI + API)
* CI-ready execution
* Stability management strategies

Target Role: **Middle QA Engineer (Automation-focused)**

---

