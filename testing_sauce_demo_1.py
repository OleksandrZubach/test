from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com.ua/?hl=uk")
time.sleep(3)

element = driver.find_element(By.CSS_SELECTOR, ".gLFyf")

element.click()
element.send_keys("sauce demo")
element.send_keys(Keys.RETURN)
element2 = driver.find_element(By.CSS_SELECTOR, ".LC20lb")
element2.click()


element2 = driver.find_element(By.CSS_SELECTOR, "#user-name")

element2.click()
element2.send_keys("standard_user")
element2.send_keys(Keys.RETURN)
# element2 = driver.find_element(By.CSS_SELECTOR, ".LC20lb")
time.sleep(3)
element3 = driver.find_element(By.CSS_SELECTOR, "#password")
element3.click()
element3.send_keys("secret_sauce")
element3.send_keys(Keys.RETURN)
time.sleep(3)

assert "Products" in driver.page_source
result = driver.find_element(By.CSS_SELECTOR,".product_label")
assert result.text == "Products"

driver.quit()