# GUVI Automation Testing Project

## Overview
This project automates the testing of the [GUVI web application](https://www.guvi.in) using **Python**, **Selenium**, and **pytest**, following the **Page Object Model (POM)** structure.  
It validates key functionalities such as page load, UI element visibility, navigation, login/logout flows, and menu accessibility.

---

## Objectives
- Verify URL accessibility and page load.
- Validate correct webpage title.
- Check visibility and clickability of Login and Sign-Up buttons.
- Validate navigation to login and sign-up pages.
- Test login functionality with valid and invalid credentials.
- Verify menu items presence.
- Check if Dobby Guvi Assistant widget is displayed.
- Test logout functionality.

---

## Project Structure

```
guvi-automation/
├─ README.md
├─ requirements.txt
├─ pytest.ini
├─ conftest.py
├─ .gitignore
├─ pages/
│  ├─ base_page.py
│  ├─ home_page.py
│  └─ login_page.py
├─ tests/
│  └─ test_guvi.py
├─ utils/
│  └─ logger.py
└─ .github/
   └─ workflows/
      └─ ci.yml
```

---

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/guvi-automation.git
cd guvi-automation
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Running Tests

### Run All Tests
```bash
pytest
```

### Run with Specific Browser
```bash
pytest --browser firefox
```

### Run Headless Mode
```bash
pytest --headless
```

### Run Specific Test File
```bash
pytest tests/test_guvi.py
```

### Run with Marker
```bash
pytest -m smoke
```

---

## CI/CD Integration
This project includes a **GitHub Actions** workflow in `.github/workflows/ci.yml` that runs tests automatically on push or pull request.

---

## Best Practices Followed
- **Page Object Model (POM)** for maintainable test scripts.
- **Cross-browser support** for Chrome and Firefox.
- **Headless mode** option for faster CI execution.
- **Logging** for debugging test runs.
- **Exception handling** for test resilience.

---

## Notes
- **Credentials**: For valid login tests, set `VALID_EMAIL` and `VALID_PASSWORD` in your environment variables or CI secrets.
- **Locator Updates**: If GUVI UI changes, update element locators in the `pages/` folder.
- **Reporting**: Integrate `pytest-html` or Allure for HTML reports if needed.

---

## License
This project is for educational purposes. All rights related to the GUVI website belong to **GUVI GEEK NETWORK PVT LTD**.
