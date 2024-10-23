# Automate user registration on an E-commerce site

from selenium.webdriver.common.by import By
import EcomTest  # Find this module in the repository
import getpass

driver = EcomTest.open_browser()
EcomTest.go_to_homepage(driver)

acc_btn = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
acc_btn.click()

email = getpass.getpass("Email: ")  # Enter email id for registration
login_field = driver.find_element(By.XPATH, '//*[@id="reg_email"]')
login_field.send_keys(email)

register_btn = driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[2]/form/p[3]/button')
register_btn.click()

try:
    logout_btn = driver.find_element(By.XPATH, '//*[@id="post-10"]/div/div/div/p[1]/a')
except:
    raise Exception('User not logged-in after registration.')

if logout_btn.is_displayed():
    print('PASS')
else:
    raise Exception('User not logged-in after registration.')

expected_msg = 'An account is already registered with your email address.'

try:
    user_exist = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li').text
    raise Exception('User already exist')
except:
    print('PASS')

if driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li').text == expected_msg:
    print('User already exist.')
else:
    print('PASS')
