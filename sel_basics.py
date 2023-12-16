from selenium import webdriver


driver = webdriver.Chrome
driver.get("http://agmarknet.nic.in/mark2_new.asp")

textinput = driver.find_element_by_name('cmm')
textinput.send_keys("banana")

button_name = "Go3"
button = driver.find_element_by_name(button_name)
button.click()
