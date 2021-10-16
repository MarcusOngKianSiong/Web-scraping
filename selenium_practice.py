from selenium import webdriver
browser = webdriver.Firefox()

browser.get('https://inventwithpython.com')
x = browser.find_element_by_class_name('email')
x.click()
x.send_keys('Something here')
x.submit()
browser.refresh