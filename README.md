# Automated Login Test

## Overview
This project provides an automated test for the login functionality of the website [EOS Bank](https://web.eos.bnk-il.com/auth). The test verifies the presence and functionality of login elements and simulates a login attempt using Selenium WebDriver.

## Technologies Used
- Python 3.x
- Selenium WebDriver
- Google Chrome & Chromedriver

## Installation & Setup
1. **Install Python** (if not already installed):  
   Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies:**  
   Run the following command to install Selenium:
   ```bash
   pip install selenium
   ```

3. **Download & Set Up Chromedriver:**  
   - Download Chromedriver from [here](https://chromedriver.chromium.org/downloads).
   - Ensure that the Chromedriver version matches your Chrome browser version.
   - Add the Chromedriver executable to your system PATH or place it in the project directory.

## Running the Test
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Run the test script:
   ```bash
   python test_login.py
   ```

## Test Details
The script performs the following actions:
- Navigates to the login page.
- Locates the username and password fields.
- Inputs test credentials (`john_doe@company.con` / `123456`).
- Clicks the login button.
- Waits for the response and checks if login was successful (assuming a positive scenario for testing purposes).

## Expected Outcome
Since real credentials are not provided, the script does not verify actual login success but assumes a successful login scenario.

## Notes
- Ensure that Google Chrome and Chromedriver are correctly installed.
- Update element locators if the webpage structure changes.
- Consider integrating the test with a CI/CD pipeline for automated execution.

## Contact
For any issues or questions, please contact the repository owner.

