# Test case: 'Coupon "xyz" does not exist!'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

# Set up Chrome options for the WebDriver 
def open_browser():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver

# Navigate to the specified homepage of the eCommerce site
def go_to_homepage(driver):
    driver.get('http://localhost:10004/')

# Find the "Add to Cart" button and click it
def add_first_item_to_cart(driver):
    first_add_btn = driver.find_element(By.CLASS_NAME, 'add_to_cart_button')
    first_add_btn.click()

# Navigate to the cart page
def go_to_cart(driver):
    driver.get('http://localhost:10004/cart/')

# Click the button to apply the coupon
def apply_coupon(driver, coupon_code):
    coupon_arrow = driver.find_element(By.CLASS_NAME, 'wc-block-components-panel__button')
    coupon_arrow.click()
    coupon_field = driver.find_element(By.ID, 'wc-block-components-totals-coupon__input-0')
    coupon_field.send_keys(coupon_code)
    apply_btn = driver.find_element(By.CLASS_NAME, 'wc-block-components-button__text')
    apply_btn.click()

# Look for an item in the cart if not found 'Retry'
def verify_cart_has_item(driver):
    for i in range(5):
        try:
            driver.find_element(By.CLASS_NAME, 'wc-block-cart-items__row')
            print('item found')
            return
        except NoSuchElementException:
            print('Item not in cart. Retrying after 2 seconds')
            time.sleep(2)
            driver.refresh()

# Retrieve and return the error message displayed for the coupon
def display_error_msg(driver):
    return driver.find_element(By.XPATH, '//*[@id="post-8"]/div/div/div[4]/div/div/div[3]/div[1]/div[1]/div/div[2]/div/div/div/div/p').text


if __name__ == '__main__':
# Main execution block
    driver = open_browser()
    go_to_homepage(driver)
    add_first_item_to_cart(driver)
    go_to_cart(driver)
    verify_cart_has_item(driver)
    apply_coupon(driver, 'xyz')
    err_msg = display_error_msg(driver)
    expected_msg = 'Coupon "xyz" does not exist!'
    
    # Assert that the error message is as expected
    assert err_msg == expected_msg, f'Unexpected error message: {err_msg}'
    print('PASS')
