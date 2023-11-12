from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://www.python.org"

driver = webdriver.Chrome()
driver.get(url)

# html = driver.page_source
#
# with open('python.html', 'w') as file:
#     file.write(html)

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")
# links = section.find_elements(By.NAME, "li")
event_dictionary = {}

for index, event in enumerate(events):
    time_long = event.find_element(By.TAG_NAME, "time").get_attribute("datetime")
    time = time_long.split("T")[0]
    title = event.find_element(By.TAG_NAME, "a").text
    temp_dict = {}
    temp_dict[f'{time}'] = title
    event_dictionary[f'{index}'] = temp_dict

print(event_dictionary)


driver.quit()