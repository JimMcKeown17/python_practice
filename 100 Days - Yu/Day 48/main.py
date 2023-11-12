from selenium import webdriver
from selenium.webdriver.common.by import By
url_orig = "https://www.amazon.com/Coding-Kids-Python-Awesome-Activities/dp/1641521759/ref=sr_1_6?crid=1G0PR6VPBK61T&keywords=coding+for+kids&qid=1699194293&sprefix=coding+for+kids%2Caps%2C79&sr=8-6"
url = "https://www.amazon.com/Beats-Fit-Pro-Cancelling-Built/dp/B09JL41N9C?ref_=Oct_DLandingS_D_ffbe9645_0"
url_python = "https://www.python.org"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get(url_python)

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# price_dollar = driver.find_element(By.CLASS_NAME, 'a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, 'a-price-fraction')
print(doc_link.text)
# print(f"{price_dollar.text}.{price_cents.text}")
driver.quit()



