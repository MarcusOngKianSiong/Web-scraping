import requests
import bs4
response_object = requests.get('https://research.aimultiple.com/web-scraping-for-finance/')
data = response_object.text

bs = bs4.BeautifulSoup(data,'html.parser')
# Problem: Used p tag to locate it, but there are too many results
# Try: Get the specific section that holds all the data you need, break it into its logical components again

specifics = bs.select('.content')

# extract the name of the item you seek
x = specifics[0].find_all('h3')

# extract the description of the item you seek
list_of_items = {}
for y in x:
    list_of_items[y.getText()] = y.find_next_sibling().getText()

with open('something.txt','a') as file:
    for key,value in list_of_items.items():
        file.write(key+'\n'+value+'\n\n')






