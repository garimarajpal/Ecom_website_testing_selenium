# Automate user registration on an E-commerce site

from selenium.webdriver.common.by import By
import EcomTest  # Ensure this module is included in the repository
import getpass

# Open the browser and navigate to the homepage
driver = EcomTest.open_browser()
EcomTest.go_to_homepage(driver)

# Click on the account button to initiate registration
acc_btn = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
acc_btn.click()

# Prompt user for email input for registration
email = getpass.getpass("Email: ")  # Enter email id for registration
login_field = driver.find_element(By.XPATH, '//*[@id="reg_email"]')
login_field.send_keys(email)

# Click the register button
register_btn = driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[2]/form/p[3]/button')
register_btn.click()

# Check if user is logged in after registration
try:
    logout_btn = driver.find_element(By.XPATH, '//*[@id="post-10"]/div/div/div/p[1]/a')
except:
    raise Exception('User not logged-in after registration.')

# Verify logout button is displayed, indicating a successful login
if logout_btn.is_displayed():
    print('PASS')
else:
    raise Exception('User not logged-in after registration.')

# Expected message for an existing user
expected_msg = 'An account is already registered with your email address.'

# Check for existing user message
try:
    user_exist = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li').text
    raise Exception('User already exist')
except:
    print('PASS')

# Verify the message for an existing account
if driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li').text == expected_msg:
    print('User already exist.')
else:
    print('PASS')
