from selenium import webdriver
from selenium.webdriver.common.by import By


'''
# Selenium

driver = webdriver.Firefox()
driver.get('https://learning.oreilly.com/library/view/automate-the-boring/9781098122584/xhtml/toc01.xhtml')


'''


# sys
'''
import sys
print(type(sys.argv[1:]))

x = ['something','nothing']
print("xxx".join(x))
'''

import project_2_functions as testing

print(testing.extract_url('/url?q=https://www.forbes.com/sites/bernardmarr/2019/06/03/5-amazing-examples-of-natural-language-processing-nlp-in-practice/&sa=U&ved=2ahUKEwjEtaihyeHzAhXOYisKHQOzDkkQFnoECAgQAg&usg=AOvVaw2IaniwIYEofrmlXKj_Hgb_'))