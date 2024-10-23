from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def open_browser():
    chrome_options = Options()

    # Keep the browser open after the script finishes running
    chrome_options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver

# Navigate to the specified homepage of the eCommerce site
def go_to_homepage(driver):
    driver.get('http://localhost:10004/')

# This block executes only if the script is run directly
if __name__ == '__main__':
    print('This is a test module')
