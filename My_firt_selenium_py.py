from selenium import webdriver
driver = webdriver.Chrome(executable_path="../resources/chromedriver.exe")
driver.maximize_window()
driver.get("http://selenium-examples.nichethyself.com")
driver.find_element_by_id("loginname").send_keys("stc123")
driver.find_element_by_id("loginpassword").send_keys("12345")
driver.find_element_by_id("loginbutton").click()
#modify
driver.close()
