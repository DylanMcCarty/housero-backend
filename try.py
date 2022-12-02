# import requests
# from bs4 import BeautifulSoup
# import numpy as np
# import pandas as pd
# import regex as re
# import lxml
# from lxml.html.soupparser import fromstring
# import prettify
# import numbers
# import htmltext
# from pprint import pprint as pp

# headers = {
#     'authority': 'www.zillow.com',
#     'accept': '*/*',
#     'accept-language': 'en-US,en;q=0.9',
#     'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
# }

# with requests.Session() as session:
#     city = 'winchester-ky/'
#     page = 1
#     url = ''
#     url = 'https://www.zillow.com/homes/for_sale/' + city + f'{page}_p'
#     response = session.get(url, headers=headers)




# soup = BeautifulSoup(response.content, 'html.parser')

# df = pd.DataFrame()


# for i in soup:
#     price = soup.find_all('span', { 'data-test' : 'property-card-price'})
#     # address = soup.find_all ('b',)
#     # beds = list(soup.find_all("span"))
#     # details = soup.find_all('div', {'class' : 'list-card-details'})
#     # home_type = soup.find_all('div', {'class' : 'list-card-footer'})
#     # last_updated = soup.find_all('div', {'class' : 'list-card-top'})
#     # brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
#     # link = soup.find_all(class_= 'list-card-link')


#     df['price'] = price
#     # df['address'] = address
#     # df['beds'] = beds



# df['price'] = df['price'].astype('str')
# # df['beds'] = df['beds'].astype('str')


# df = df[['price']]
# # df = df[['beds']]

# pp(df)