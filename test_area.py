from selenium import webdriver
from selenium.webdriver.common.by import By
'''
driver = webdriver.Firefox()
driver.get('https://learning.oreilly.com/library/view/automate-the-boring/9781098122584/xhtml/toc01.xhtml')

#x = driver.find_element_by_xpath("//form[@id='signup-form']")
y = driver.find_elements_by_xpath("//div[@id='sbo-rt-content']/descendant::p/a[text()]")          # Return every element that is a parent

y = [i.text for i in y]

for x in y:
    print(x)
'''

with open('something.txt','a') as file:
    for x in range(10):
        file.write(str(x)+'\n')
