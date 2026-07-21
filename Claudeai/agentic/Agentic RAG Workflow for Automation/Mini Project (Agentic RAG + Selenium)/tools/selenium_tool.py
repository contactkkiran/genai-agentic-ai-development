from selenium import webdriver
from selenium.webdriver.common.by import By


def run_selenium_test(test_name: str) -> str:
    if test_name == "login":
        driver = webdriver.Chrome()
        driver.get("https://example.com/login")

        try:
            driver.find_element(By.ID, "username").send_pip install webdriver-managerkeys("testuser")
            driver.find_element(By.ID, "password").send_keys("password123")
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            result = "Login test passed"
        except Exception as e:
            result = f"Login test failed: {str(e)}"
        finally:
            driver.quit()
        return result
    return f"Unknown test: {test_name}"
