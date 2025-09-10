

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")
# Login steps
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
# Add a product to the cart
driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
# Verify cart count
cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
assert cart_count == "1", "Cart count mismatch!"
print("Test Passed: Product added to cart successfully.")
driver.quit()