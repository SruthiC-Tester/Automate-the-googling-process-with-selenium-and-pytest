
# 🔍 Selenium Google Search Automation

## 📖 Overview

This project contains automated test scripts using **Selenium WebDriver** in Python to:

* Open Google.
* Perform a search with the keyword `"selenium"`.
* Open the first search result.
* Verify if it navigates to the official Selenium website.

It demonstrates basic usage of Selenium for browser automation, web element interaction, assertions, and explicit waits.

---

## ✨ Features

* Navigates to Google and validates the page title.
* Searches for a keyword (`"selenium"`) and verifies the search results page.
* Clicks on the first search result and verifies it leads to [selenium.dev](https://www.selenium.dev/).
* Implements **explicit waits** using `WebDriverWait` and `expected_conditions`.

---

## 🛠️ Technologies Used

* **Python 3.8+**
* **Selenium 4+**
* **Chrome WebDriver**

---

## ✅ Prerequisites

Make sure the following are installed on your system:

1. **Python 3.8+**
   Download: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Google Chrome**
   Download: [https://www.google.com/chrome/](https://www.google.com/chrome/)

3. **ChromeDriver**
   Download: [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
   Ensure it's added to your system's PATH.

4. **Selenium Library**
   Install using pip:

   ```bash
   pip install selenium
   ```

---

## 📁 Project Structure

```
selenium_google_search/
│
├── tests/
│   ├── test_google_search.py    # Contains all Selenium test functions
│
├── README.md                    # Project documentation
│
└── requirements.txt             # (Optional) Python dependencies list
```

Example `requirements.txt`:

```txt
selenium>=4.0.0
```

---


