# Scrapping the local Ecom site for products and their prices

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://localhost:10004/')
driver.implicitly_wait(10)

all_products = driver.find_elements(By.CLASS_NAME, 'product-type-simple')
print(f'Number of products: {len(all_products)}')

all_products_price = []
for product in all_products:
    price_elm = product.find_element(By.CSS_SELECTOR, 'span.amount')
    price = price_elm.text

    name_elm = product.find_element(By.CSS_SELECTOR, 'h2.woocommerce-loop-product__title')
    name = name_elm.text
    all_products_price.append({name: price})
#    print(price)
#    print(name)

print(len(all_products_price))
print(all_products_price)
