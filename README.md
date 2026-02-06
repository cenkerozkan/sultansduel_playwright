# Sultan's Duel - Playwright Test Automation

A Playwright-based test automation project for **Sultan's Duel**, a browser-based card game. This project serves as a learning playground for Playwright testing best practices and Page Object Model (POM) architecture.

## 📋 Project Overview

**Sultan's Duel** is a hobby project card game built by a friend. This repository contains automated UI tests using Playwright with Python, demonstrating:

- ✅ Page Object Model (POM) pattern implementation
- ✅ Async/await patterns with pytest-asyncio
- ✅ Component-based architecture
- ✅ Best practices for browser automation
- ✅ Organized test structure and fixtures

## 🎯 Purpose

This is a **training and learning project** to:
- Master Playwright automation for web applications
- Practice test automation design patterns
- Build scalable and maintainable test suites
- Explore async testing with Python

## 🏗️ Project Structure

```
sd_playwright/
├── src/
│   └── ui/
│       ├── pages/           # Page Object Models
│       │   ├── base_page.py
│       │   └── login_page.py
│       └── components/      # Reusable UI components
│           ├── base_component.py
│           └── navbar.py
├── tests/
│   ├── conftest.py         # Pytest fixtures and configuration
│   └── ui/                 # UI test files
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Python dependencies
└── README.md
```

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd sd_playwright
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install Playwright browsers**
```bash
playwright install
```

## 🔐 Environment Configuration

Create a `.env` file in the project root:

```env
USER_EMAIL=your_email@example.com
USER_PASSWORD=your_password
BASE_URL=https://www.sultansduel.com
```

Use `.env.example` as a template.

## 🚀 Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/ui/test_login.py
```

### Run tests by marker
```bash
pytest -m smoke           # Run smoke tests
pytest -m "ui and not slow"  # Run UI tests excluding slow tests
```

### Run with verbose output
```bash
pytest -v
```

### Run with headed browser (see the browser)
Update `conftest.py` to set `headless=False`:
```python
browser = await p.chromium.launch(headless=False)
```

## 📝 Test Markers

Available test markers defined in `pytest.ini`:

- `@pytest.mark.asyncio` - Async test
- `@pytest.mark.smoke` - Smoke tests
- `@pytest.mark.regression` - Regression tests
- `@pytest.mark.ui` - UI tests
- `@pytest.mark.slow` - Slow running tests

## 🏗️ Architecture

### Page Object Model (POM)

Each page is represented as a class with:
- **Locators** - Elements on the page
- **Actions** - Methods that interact with the page
- **Assertions** - Methods that verify page state

Example:
```python
class LoginPage(BasePage):
    async def login(self, email: str, password: str):
        """Complete login flow"""
        await self.fill_email(email)
        await self.fill_password(password)
        await self.click_login()
```

### Components

Reusable UI components (Navbar, dialogs, etc.) are stored in `src/ui/components/`.

## 📚 Key Technologies

- **[Playwright](https://playwright.dev/)** - Browser automation framework
- **[Pytest](https://pytest.org/)** - Test framework
- **[pytest-asyncio](https://pytest-asyncio.readthedocs.io/)** - Async support for pytest
- **[Python-dotenv](https://github.com/theskumar/python-dotenv)** - Environment variable management

## 🔍 Testing Best Practices Demonstrated

✅ Page Object Model pattern  
✅ Async/await usage  
✅ Fixture-based setup and teardown  
✅ Semantic locators (get_by_role, get_by_text)  
✅ Component reusability  
✅ Test organization and markers  

## 🎓 Learning Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://playwright.dev/python/docs/pom)
- [Async Testing](https://pytest-asyncio.readthedocs.io/)

## 📝 Notes

- This project is for **educational purposes** and practice
- Tests are written against **Sultan's Duel**, a hobby project
- Focus is on learning automation patterns, not production-ready test coverage

## 🤝 Contributing

Feel free to improve the test suite, add new tests, or refactor existing code as part of your learning journey!

## 📄 License

This project is for educational purposes.

---

**Happy Testing! 🎮✅**