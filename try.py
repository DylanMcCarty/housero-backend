import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import regex as re
import lxml
from lxml.html.soupparser import fromstring
import prettify
import numbers
import htmltext
from pprint import pprint as pp
import json

headers = {
    'authority': 'www.redfin.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

with requests.Session() as session:
    zipcode = '40391'
    page = 1
    end_page = 3


    url = ''
    url_list = []

    while page <= end_page:
        url = 'https://www.redfin.com/zipcode/' + f'{zipcode}' + '/filter/property-type=house/' + f'page-{page}'
        url_list.append(url)
        page += 1
        # response = session.get(url, headers=headers)

    request = ''
    request_list = []

    for url in url_list:
        request = session.get(url, headers=headers)
        request_list.append(request)
        
soup = ''
soup_list = []

for request in request_list:
    soup = BeautifulSoup(request.content, 'html.parser')
    soup_list.append(soup)


df_list = []

for soup in soup_list:
    df = pd.DataFrame()
    for i in soup:
        address = soup.find_all(class_ = 'collapsedAddress primaryLine')
        price = soup.find_all(class_ = 'homecardV2Price')
        beds = list(soup.find_all('div', class_='HomeStatsV2'))



        df['address'] = address
        df['price'] = price
        df['beds'] = beds

    urls = []

    df_list.append(df)

#concatenates all pages of data onto eachother so that all data cmes back correctly
df = pd.concat(df_list).reset_index().drop(columns='index')


#sets values as a string which they must be for them to be converted into a json object
df['address'] = df['address'].astype('str')
df['price'] = df['price'].astype('str')
df['beds'] = df['beds'].astype('str')


# this just replaces everything in the string that contains things that are not the values i want with an empty string and sets those values equal to an altered string
df.loc[:, 'address'] = df.loc[:, 'address'].replace('</span>', '', regex=True)
df.loc[:, 'address'] = df.loc[:, 'address'].replace('<span class=\\"collapsedAddress primaryLine\\" data-rf-test-id=\\"abp-streetLine\\">', '', regex=True)
df.loc[:, 'price'] = df.loc[:, 'price'].replace('</span>', '', regex=True)
df.loc[:, 'price'] = df.loc[:, 'price'].replace('<span class=\\"homecardV2Price\\" data-rf-test-name=\\"homecard-price\\">', '', regex=True)
df.loc[:, 'beds'] = df.loc[:, 'beds'].replace('<div class=\\"HomeStatsV2 font-size-small\\"><div class=\\"stats\\">', '', regex=True)
df.loc[:, 'beds'] = df.loc[:, 'beds'].replace('</div><div class=\\"stats\\">', ' ', regex=True)
df.loc[:, 'beds'] = df.loc[:, 'beds'].replace('</div><div class=\\"stats\\">', ' ', regex=True)
df.loc[:, 'beds'] = df.loc[:, 'beds'].replace(' Sq. Ft.</div></div>', '', regex=True)
df.loc[:, 'beds'] = df.loc[:, 'beds'].replace(' Beds', '', regex=True)
df.loc[:, 'beds'] = df.loc[:, 'beds'].replace(' Baths', '', regex=True)
df.loc[:, 'beds'] = df.loc[:, 'beds'].replace(' Bed', '', regex=True)
df.loc[:, 'beds'] = df.loc[:, 'beds'].replace(' Bath', '', regex=True)



#selects everything to be returned only that contains the original zipcode
df = df[df['address'].str.contains(zipcode)]

df[['beds', 'baths', 'sq_feet']] = df.beds.str.split(expand=True)

#simply prints a json object of the dataframe using json loads and dumps to stringify the object and turn it into json
# print(json.dumps(json.loads(df.to_json(orient='index')), indent=2))

