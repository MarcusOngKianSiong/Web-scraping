# Description of the problem to solve

'''
Open multiple top searches in Google on different tabs on google chrome through a command line.
Type a search term on the command line.
Have the computer automatically open a browser with all the top search results in new tabs

Process:
1. Get search results from cmd
2. Open up browser
3. Go to the website
3. Type in the keywords
4. Identify the top search results
5. Ctrl enter the link

What tools can fulfill this process?
    - Webbrowser
    - Requests
    - bs4
    - sys
'''

import webbrowser
import requests
import bs4
import sys
import time
import project_2_functions as functions

search_link = 'https://Google.com/search?q='

# Get search results from command line and combine the various arguments into a string
search = sys.argv[1:]
search = "+".join(search)

# Open browser and go to the search result page
webbrowser.open(search_link+search)

# Retrieve the google search page
search_page = requests.get(search_link+search)

# Parse the search page to identify the relevant links
'''
Problem encounteded: bs4 mentioned that it has no attribute beautifulsoup.
Method: Look for the solution online
            - 
Solution: Changing beautifulsoup into BeautifulSoup

Problem encountered: select method is returning a list with no values when I am using class attribute value to locate the elements
Method: 
    - Use different type of methods
    - Use reasoning: If using class gives me an empty list, then it might be that parsed_search_page might miss out on some information when extracting
        - Test out this reasoning: Check use other ways of locating the elements (tags, text)
        - Realized that the elements I am looking for exist
        - This means that parsed_search_page did not miss out on any information
        - Check the attributes (class) of the element I am targeting
        - FOUND THE PROBLEM: Turns out that the attribute value is different from what is shown on the browser.
Solution:
    - 

Problem: Used a method of an object and the error states that it is a none type
Solve this problem:
    1. Review your understanding
        - Beautifulsoup object parses the raw html in text form
        - You can use other methods on the beautifulsoup object to specifically identify the element you are looking for
        - These other methods will return a tag object
        - Tag object goes one step deeper and allow you to extract any information within that specific element you have extracted
    2. Identify the part of your understanding that does not match with the real world evidence.
        - Tag object goes one step deeper
    3. Look up what you can actually do with tag object and zone in on those that are relevant
        - retrieving attribute value: tag object['attribute value']             // Called a subscript notation
        - Finding the parent of a tag: tag object.parent 
        - find the tag name: tag object.name
'''

parsed_search_page = bs4.BeautifulSoup(search_page.text,'html.parser')      # The entire html page parsed

x = parsed_search_page.find_all('h3')                # a list of specific elements whose parent's attribute contain the link that represents the top search results in Google
top_search_results = []
for b in x:
    parent = b.parent
    if parent.name == 'a':
        #top_search_results.append(parent['href'])
        top_search_results.append(parent['href'])
        
    
# Open new tabs and go to the each page for each tab
'''
Problem: THe links extracted are wrong, thereby causing me to open up Internet Explorer instead of google chrome

SOlving the problem:
    - Find all the attributes of the element I am looking for to see if there is a correct one: .attrs          -> No. There is only one attribute for the elements I am targeting (href) and all the values does not help me get to the specific webpage I want
    - Find a way to turn the bad link into the supposed link: 
        - It seems like by taking part of the bad link, I am able to go to the webpage I am suppose to go to when I press the money.
        - What are the components of a URL?
            - Scheme    -> Protocol used to get information from the web                -> https://
            - Host      -> Server that holds the data                                   -> google.com
            - Path      -> location of the document within the server                   -> /xyz/x/something.html
            - Query     -> String of information that the specific document can use     -> ?q=1&w=2
        - Which part of the extracted link works?
            - scheme, host, path.
        - Based on the observed link, how can you extract what you need?
            - Start from https://
            - end before the first &
        - Write out the code to extract the part of the string that contains the url you need
            - A function called extract url has been created in project_2_functions.py
        - Create a list of URLs that work
            - 
'''
# Use back top_search_results_list, SOLVED THE PROBLEM OF BAD URL
for index,bad_url in enumerate(top_search_results):
    top_search_results[index] = functions.extract_url(bad_url)

# Open the links in the browser
for working_url in top_search_results:
    webbrowser.open(working_url)




