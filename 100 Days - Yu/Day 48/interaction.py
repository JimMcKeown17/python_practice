from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set the options for Chrome:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Now pass the options when initializing the driver:
driver = webdriver.Chrome(options=chrome_options)

url = "https://secure-retreat-92358.herokuapp.com/"

driver.get(url)

# Find the search bar and send the keys 'Python'
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Qhawe")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Dlamini")
email = driver.find_element(By.NAME, "email")
email.send_keys("qhawe@gmail.com")
button = driver.find_element(By.CLASS_NAME, "btn")
button.send_keys(Keys.ENTER)  # If you also want to submit the search





search.send_keys(Keys.ENTER)  # If you also want to submit the search
