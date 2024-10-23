from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import pdb

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get('http://localhost:10004/')

# Finding Elements By.ID

cart = driver.find_element(By.ID, "site-header-cart")
print(cart)
print(type(cart))
cart_text = cart.text
print(cart_text)

# accessing search field using BY.ID

search_field = driver.find_element(By.ID, "woocommerce-product-search-field-0")
search_field.send_keys('Hoodie')
search_field.send_keys(Keys.ENTER)

# By.XPATH

my_acc = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/nav/div[1]/ul/li[4]")
my_acc.click()

pdb.set_trace()
# driver.quit()
# driver.close()
