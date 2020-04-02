from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('https://www.flipkart.com/search?q=samsung+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=samsung+mobiles%7CMobiles&requestId=fff40bfd-a009-4ac8-9e22-fb50f0cb71de&as-searchtext=samsung+s&p%5B%5D=facets.price_range.from%3D20000&p%5B%5D=facets.price_range.to%3DMax').text
soup = BeautifulSoup(source, 'lxml')
csv_file = open('flipkart_scrape', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Phone Name', 'Rating', 'Specifications', 'Current Price', 'Original Price'])
for phone in soup.find_all('div', class_='_1UoZlX'):
    try:      
        name = phone.find('div', class_ = '_3wU53n').text
        rating = phone.find('div', class_ = 'hGSR34').text
        specs = phone.find('div', class_ = '_3ULzGw').text
        cp = phone.find('div', class_ = '_1vC4OE _2rQ-NK').text
        op = phone.find('div', class_  = '_3auQ3N _2GcJzG').text
    except:
        pass
    csv_writer.writerow([name,rating,specs,cp[1:],op[1:]])
csv_file.close()

