from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (Ensure Google Chrome and ChromeDriver are installed)
driver = webdriver.Chrome()

try:
    # Open the login page
    driver.get("https://web.eos.bnk-il.com/auth")
    time.sleep(2)  # Wait for the page to load

    # Locate the username field by ID and enter credentials
    username_field = driver.find_element(By.ID, ":r1:")  # Using ID for better accuracy
    username_field.send_keys("john_doe@company.con")

    # Locate the password field by ID and enter credentials
    password_field = driver.find_element(By.ID, ":r2:")  # Using ID for better accuracy
    if password_field.get_attribute("type") == "password":  # Ensuring the field is of type 'password'
        password_field.send_keys("123456")
    else:
        print("⚠️ Password field is not recognized as a 'password' input!")

    # Locate the login button using type='submit' and click it
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Wait for the response from the server
    time.sleep(5)

    # Verify if login was successful (Assuming success for test purposes)
    if "dashboard" in driver.current_url:
        print("✅ Login successful (Test case assumption)")
    else:
        print("⚠️ Login might have failed (Test case assumption)")

except Exception as e:
    print(f"🚨 Test encountered an error: {e}")

finally:
    driver.quit()  # Close the browser
