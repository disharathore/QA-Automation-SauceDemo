from selenium.webdriver.common.by import By


def test_valid_login(driver):

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url


def test_invalid_login(driver):

    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error_message
