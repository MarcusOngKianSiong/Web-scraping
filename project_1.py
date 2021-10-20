from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

firefox = webdriver.Firefox()
firefox.get('https://www.oreilly.com/')

# I am not certain on how to find the element that I am seeking usingselenium
# Method to solve it: 
'''
1. Find out what you can understand
    - Look at all the find element/elements method and understand what value they look for and return
2. Try to use the information have successfully processed to chart a path towards getting what you need
    - Use find_elements_by_tag_name to find all the link elements
    - Find one where the text states sign in
'''

x = firefox.find_elements_by_tag_name('a')
for count,y in enumerate(x):
    if y.text == 'SIGN IN':
        x[count].click()
        break

# Problem encountered: the elements held by firefox object belongs to the initial webpage
# How do I change webpage held by the object?
'''
My understanding was wrong. 
I thought that the webpage held by the webdriver object (firefox variable) only holds the webpage of the first webpage initialized by get() method. 
However, it is not the case as after using find_elements_* methods, the return values (elements on the webpage) when both webpage 
were being displayed through the usage of get shows different number of elements and different attribute values.

Sub problems encountered: Nearly identical identifiers makes it hard to distinguish between two elements
Some methods of location the elements is more effective than others. Using tags or certain identifiers
will not be very effective as there is too much similar names, which makes it easy to miss out details. 
Therefore, use locators that is not easy to duplicate. One example is the text used within the tag (<p>THIS TEXT</p>).
'''
x = firefox.find_elements_by_tag_name('input')
for count,y in enumerate(x):
    if y.get_attribute('name') == 'email':
        x[count].click()
        x[count].send_keys('1902902D@student.tp.edu.sg')
        x[count].send_keys(Keys.TAB)
        time.sleep(1)
        break
    
x = firefox.find_element_by_class_name('orm-Button-btnContentWrap')
x.click()
time.sleep(2)               # Need some time for the site to load before they can pull out the html
print(firefox.current_url)

if firefox.current_url == 'https://login.microsoftonline.com/25a99bf0-8e72-472a-ae50-adfbdf0df6f1/saml2':
    x = firefox.find_element_by_id('i0116')
    username = input()

    x.send_keys(username)
    y = firefox.find_element_by_id('idSIButton9')
    y.click()
    time.sleep(1)
    x = firefox.find_element_by_id('i0118')
    y = firefox.find_element_by_id('idSIButton9')
    password = input()

    x.send_keys(password)
    y.click()
    
    time.sleep(1)
    y = firefox.find_element_by_id('idSIButton9')
    y.click()

# Type something into the texbox when the id of the textbox keeps changing
x = firefox.find_elements_by_tag_name('input')
for count,y in enumerate(x):
    if y.get_attribute('placeholder') ==  'Search for books, videos, live events, and more':
        #book = input('Book to extract: ')
        book = 'automate'
        y.send_keys(book)

# Find the element with the title as text
# Problem: Cannot pinpoint the exact element that I need to click due to not having a unique identifier
'''
Solution:
1. Find a potential way of getting the element you seek by remembering the concepts taught in web development (neighbouring element)
2. Ask google how to find the neighbour element using selenium
3. Many articles talk about something called Xpath, which is identifying elements based on its relation with other elements
4. Go learn XPath: Took me 1 day
    - Read the general description of what it does
    - Find a scenario
    - Predict an outcome from a piece of code
    - Test the code out for real
    - Repeat until all concepts are learned
5. Apply
6. Encounter problems associated with typo errors: missing characters
7. Succeed
'''
time.sleep(1)
x = firefox.find_element_by_xpath("//span[text()='titles']/following-sibling::ul/descendant::li")
x.click()

# click the continue or start button
time.sleep(5)
x = firefox.find_element_by_xpath("//a[@class='orm-Link-root startBtn--_rDV6 ']")
x.click()

# Scrap the content page
'''
1.Find the section to 

'''
time.sleep(2)
x = firefox.find_element_by_xpath("//span[@class='orm-Icon-icon icon--fKY7x  orm-icon-bullet-list ']")
x.click()

# Create the section that contains what you seek and find the element within it.
# Problem: What if there are multiple types of content page in the book?

'''
1. Create a list that contains webelement objects that link to the content page
2. Remove everything that does not contain content
3. Go to each link and extract the data on the page
4. Take the larger one
'''
# Problem: I cannot use contains on the text of an element to extract web element objects.
'''
1. Your understanding: Check your understanding of contains
    - Reinforcing previous conclusions: nodes that have axes cannot have conditions
    - the second argument in the contains function must have ''
'''
time.sleep(1)
x = firefox.find_elements_by_xpath("//ol[@class='tableOfContents--B2oHx']/descendant::h5/a[contains(text(),'CONTENTS')]")
# I have two links

# Go to each site and extract the data
'''
Problem: inserting value into a string does not work
Check the link again that is generated from y.get_attribute
the problem is that I forgot to put an f at the front: f"asfdsag{x}"
However, realized that the environment does not allow you to go to the link directly as two identical links
where one is directly accessed by copy and pasting on search bar does not work while clicking the link in the book 
works.

Another problem encountered:
Code not outputting the data on the page
Turns out, the page is not loading fast enough, therefore the code outputs nothing because the code is analyzing a blank
page at the time of loading.

Another problem encountered:
There is missing data. 
'''
data = {}
for count,page in enumerate(x):
    page.click()
    time.sleep(2)
    a = page.find_elements_by_xpath("//div[@id='sbo-rt-content']/descendant::p/a[text()]")
    data[count] = [i.text for i in a]

# Find the one with the most amount of information
length = 0
target = 0
for key,value in data.items():
    if len(value) >= length:
        target = key
        length = len(value)

# create a file that contains the data extracted
with open('data.txt','w') as file:
    for a in data[target]:
        file.write(str(a)+'\n')

