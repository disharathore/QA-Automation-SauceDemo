from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_item_to_cart(driver):


    # Login first
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Add first item to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Verify cart badge shows 1
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_badge == "1"

def test_checkout_flow(driver):

    wait = WebDriverWait(driver, 10)

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Add item
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Go to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Click checkout
    driver.find_element(By.ID, "checkout").click()

    # Wait for first name field to be visible
    wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

    # Fill details
    driver.find_element(By.ID, "first-name").send_keys("Disha")
    driver.find_element(By.ID, "last-name").send_keys("Rathore")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()

    # Finish order
    wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    driver.find_element(By.ID, "finish").click()

    # Verify confirmation
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    confirmation = driver.find_element(By.CLASS_NAME, "complete-header").text

    assert "Thank you" in confirmation
