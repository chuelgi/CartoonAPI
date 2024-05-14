import requests
from bs4 import BeautifulSoup
import pymongo
import certifi

# URL of the website to scrape
url = ['https://en.wikipedia.org/wiki/List_of_animated_television_series_of_2001']

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the website using Beautiful Soup
    main_soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the specific table within the HTML content
    table = main_soup.find('table', class_='wikitable')
    
    if table:
        # Find all rows within the table

        #list of dictionaries
        cartoons_data= []

        rows = table.find_all('tr')
        
        # Iterate through each row and extract data
        for row in rows:
            # Find all cells within the row
            cells = row.find_all('td')
            
            
            if len(cells) >= 6:
                # Extract data from cells and create a dictionary for each cartoon
                cartoon_data = {
                    'title': cells[0].text.strip(),
                    'seasons': int(cells[1].text.strip()) if cells[1].text.strip() else None,  # Convert to int if not empty, else None
                    'episodes': int(cells[2].text.strip()) if cells[2].text.strip() else None,  # Convert to int if not empty, else None
                    'country': cells[3].text.strip(),
                    'years_active': cells[4].text.strip(),
                    'network': cells[5].text.strip(),
                    'animation_type': cells[6].text.strip() if len(cells) >= 7 else ''  # Additional check for optional field
                }
                cartoons_data.append(cartoon_data)

        print(cartoons_data)
            
    else:
        print(f'No table found on the page: {url}')
else:
    print(f'Failed to fetch data from the website: {url}')



'''
print('connecting to mongo...')
client = pymongo.MongoClient()

print('getting db...')
db = client['cartoon_db']

print('getting collection...')
collection = db['cartoons']

print('inserting...')
x = collection.insert_many(cartoons_data)

print('Data inserted successfully into the MongoDB collection.')
print(x.inserted_ids)
'''